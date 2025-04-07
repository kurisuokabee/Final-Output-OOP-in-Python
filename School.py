from abc import ABC, abstractmethod

# Abstract base class
class School(ABC):
    def __init__(self, students):
        self.students = students  # students is a Dictionary: {"Name": [grades]}

    @abstractmethod
    def display_average_grades(self):
        pass

    @abstractmethod
    def display_gpa(self):
        pass


# SchoolOne inherits from School
class SchoolOne(School):
    def display_average_grades(self):
        print("School One - Average Grades")
        for name, grades in self.students.items():
            avg = sum(grades) / len(grades)
            print(f"{name}: {avg:.2f}")

    def display_gpa(self):
        print("School One - GPA")
        for name, grades in self.students.items():
            gpa = self.calculate_gpa(grades)
            print(f"{name}: {gpa:.2f}")

    # GPA scale: 0–100 mapped to 0–4
    def calculate_gpa(self, grades):
        avg = sum(grades) / len(grades)
        return (avg / 100) * 4  

# SchoolTwo inherits from School
class SchoolTwo(School):
    def display_average_grades(self):
        print("School Two - Average Grades")
        for name, grades in self.students.items():
            avg = sum(grades) / len(grades)
            print(f"{name}: {avg:.2f}")

    def display_gpa(self):
        print("School Two - GPA")
        for name, grades in self.students.items():
            gpa = self.calculate_gpa(grades)
            print(f"{name}: {gpa:.2f}")

    # GPA scale: 0–100 mapped to 0–4
    def calculate_gpa(self, grades):
        avg = sum(grades) / len(grades)
        return (avg / 25)  

#Student Data; Dictionary: {"Name": [grades]}
students_one = {
    "Luffy": [85, 90, 78],
    "Zoro": [92, 88, 95]
}

students_two = {
    "Nami": [75, 80, 70],
    "Ussop": [89, 91, 84]
}

# Instantiate and use the classes
school1 = SchoolOne(students_one)
school2 = SchoolTwo(students_two)

#Print the average grades and gpa
school1.display_average_grades()
print("\n-----------------\n")
school1.display_gpa()

print("\n-----------------\n")

school2.display_average_grades()
print("\n-----------------\n")
school2.display_gpa()