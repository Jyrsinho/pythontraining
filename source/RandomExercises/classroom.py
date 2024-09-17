class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def sort_students_by_grade(self):
        """
       sorts students by their grade
       :return: list of students sorted by grade
       """""
        for student in self.students:
            return self.students

    def printgradequartiles(self):
        return 0

    def __str__(self):
        student_details = "\n".join(str(student) for student in self.students)
        return f"Classroom contains the following students: \n{student_details}"


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Student: (name={self.name},  grade={self.grade})"


student1 = Student("Timo", 80)
student2 = Student("Juan", 70)
student3 = Student("Sebastian", 60)
student4 = Student("Max", 30)

classroom = Classroom()
classroom.add_student(student1)
classroom.add_student(student2)
classroom.add_student(student3)
classroom.add_student(student4)

classroom.sort_students_by_grade()
print(classroom)
