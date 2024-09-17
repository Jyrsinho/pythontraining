# test classroom.py

from source.RandomExercises.classroom import Classroom, Student


class TestClassroom:
    
    def setup_method(self, method):
        print(f"Setting up {method}")
        classroom = Classroom()
        student = Student("Alice", 90)
        
    def test_add_student(student):
        classroom.add_student(student)
        
        
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        
    def test_sort_students_by_grade(self):
        assert True

    
    