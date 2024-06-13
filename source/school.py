
class TooManyStudentsException(Exception):
    pass

class Classroom:
    
    def __init__(self, teacher, students, course_title):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title
        
    def add_student(self, student):
        if len(self.students) <= 10:
            self.students.append(student)
        else:
            raise TooManyStudentsException
                
    
        