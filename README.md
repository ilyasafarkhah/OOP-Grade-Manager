# OOP-Grade-Manager
# Python OOP Grade Manager

A robust, object-oriented Python system designed to manage student records and calculate academic statistics. This project focuses heavily on data integrity, dynamic input handling, and crash prevention (Edge-Case handling).

## How the Code Works

The system architecture is strictly divided into two interacting classes to maintain the **Single Responsibility Principle**:

### 1. The `Student` Class (Data Entity)
This class represents an individual student. It is solely responsible for internal data validation and calculating personal metrics.
* **Dynamic Inputs:** Utilizes `**kwargs` in the constructor to accept an arbitrary number of subjects and scores (e.g., `math=18, physics=20`).
* **Strict Validation:** Automatically validates that names are non-empty strings and that grades fall strictly within the 0 to 100 range.
* **State Protection:** Blocks operations that could corrupt the object's state, such as attempting to delete a student's final remaining grade (which would otherwise cause a `ZeroDivisionError` during average calculations).

### 2. The `GradeManager` Class (Controller)
This class acts as the centralized grade book and system controller.
* **Instance-Based Storage:** Each `GradeManager` initializes its own independent `students_list`. This allows multiple class instances (e.g., Class A, Class B) to exist simultaneously without data collision.
* **Collision Detection:** Actively scans existing records before adding or renaming a student to prevent duplicate names in the system.
* **Aggregated Calculations:** Relies on Python's **List Comprehensions** to efficiently extract and aggregate data across all stored `Student` objects, calculating class-wide maximums, minimums, and averages.
* **Bulletproof Queries:** Evaluates queries dynamically. If a requested operation involves an empty class list or a non-existent subject, the system safely intercepts it and returns `0` instead of crashing.

## Usage Example

```python
# 1. Initialize a new, independent manager
manager = GradeManager()

# 2. Add students dynamically using kwargs
manager.add_student("Ali", math=18, physics=20)
manager.add_student("Neda", math=20, physics=19, chemistry=18)

# 3. Modify records
# Validation rules are automatically applied during updates
manager.update_student("Ali", "Alireza")

# 4. Generate Statistical Outputs
print("Class Average:", manager.average_grade())
print("Math Average:", manager.specific_average_grade("math"))

# 5. Safe Edge-Case Handling (No crashes on empty queries)
print("History Average:", manager.specific_average_grade("history"))
# Console Output: No grades found for lesson: history
# Return Value: 0
