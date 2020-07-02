class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
class Student(Person):
    def __init__(self, first_name, last_name, gpa, classes=None)
        Person.__init__(self, first_name, last_name)
        self.gpa = gpa
        if classes is None:
            self.classes = []
        else:
            self.classes = classes
            
    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
           
class Teacher(Person):
    def __init__(self, first_name, last_name, tenure, subject, students=None)
        Person.__init__(self, first_name, last_name)
        self.tenure = tenure
        self.subject = subject
        if students is None:
            self.students = []
        else:
            self.students = students
            
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)