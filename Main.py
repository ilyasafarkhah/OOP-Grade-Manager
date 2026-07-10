class Student:
    def __init__(self, name, **grades):
        if not isinstance(name, str):
            raise TypeError("Student name must be a string")
        if not name.strip():
            raise ValueError("Student name cannot be an empty string")
        if not grades:
            raise ValueError("Student grades cannot be empty")

        for lesson, score in grades.items():
            if not 0 <= score <= 100:
                raise ValueError(f"Score for {lesson} must be between 0 and 100")

        self.name = name
        self.grades = grades

    def remove_grade(self, lesson):
        if lesson in self.grades:
            if len(self.grades) <= 1:
                print("Cannot remove the last grade. A student must have at least one grade.")
                return
            del self.grades[lesson]
            print(f"Grade {lesson} removed.")
        else:
            print(f"Grade {lesson} not in grades")

    def update_grade(self, lesson, new_score):
        if lesson in self.grades:
            if 0 <= new_score <= 100:
                self.grades[lesson] = new_score
                print(f"Grade {lesson} updated to {new_score}.")
            else:
                print("Student score must be between 0 and 100")
        else:
            print(f"Grade {lesson} not in grades")

    def maximum_grade(self):
        return max(self.grades.values())

    def average_grade(self):
        return round(sum(self.grades.values()) / len(self.grades), 2)

    def minimum_grade(self):
        return min(self.grades.values())

    def __repr__(self):
        return str({"name": self.name, "grades": self.grades})


class GradeManager:
    def __init__(self):
        self.students_list = []

    def add_student(self, name, **grades):
        for student in self.students_list:
            if student.name == name:
                print(f"Student '{name}' already exists.")
                return

        try:
            student = Student(name, **grades)
            self.students_list.append(student)
            print(f"Student '{name}' added successfully.")
        except (ValueError, TypeError) as e:
            print(f"Error adding student: {e}")

    def remove_student(self, name):
        for student in self.students_list:
            if student.name == name:
                self.students_list.remove(student)
                print(f"Student '{name}' removed.")
                return
        print("Student not in list")

    def update_student(self, old_name, new_name):
        if any(s.name == new_name for s in self.students_list):
            print(f"Name '{new_name}' is already taken.")
            return

        for student in self.students_list:
            if student.name == old_name:
                student.name = new_name
                print(f"Student name updated to '{new_name}'.")
                return
        print("Student not in list")

    def maximum_grade(self):
        if not self.students_list:
            return 0
        return max(grade for student in self.students_list for grade in student.grades.values())

    def minimum_grade(self):
        if not self.students_list:
            return 0
        return min(grade for student in self.students_list for grade in student.grades.values())

    def average_grade(self):
        if not self.students_list:
            return 0
        result = [grade for student in self.students_list for grade in student.grades.values()]
        return round(sum(result) / len(result), 2)

    def specific_average_grade(self, target_lesson):
        result = [score for student in self.students_list for lesson, score in student.grades.items() if lesson == target_lesson]
        if not result:
            print(f"No grades found for lesson: {target_lesson}")
            return 0
        return round(sum(result) / len(result), 2)
