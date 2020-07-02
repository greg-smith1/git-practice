class Students:
    students={0:{"name":"admin","grades": None,"class name":None }}
    num=0
    def __init__(self, i_d, name,class_name, grades=[]):
        self.name=name
        self.grades=grades
        self.class_name=class_name
        self.i_d=i_d
        Students.students[self.i_d]={"name":self.name, "grades":self.grades, "class name":self.class_name}

    def update_grade(self, new_grade):
        self.grades.append(new_grade)

    @classmethod
    def remove_student(cls, i_d):
        del cls.students[i_d]

    @classmethod
    def create(cls, name, class_name, grades=[]):
        name1=name
        class1=class_name
        grade1=grades
        Students.num+=1
        i_d=Students.num
        student=Students(i_d, name1, class1, grade1)
        return student

    @classmethod
    def login(cls,i_d):
        if i_d in cls.students:
            # name=students[id]["name"]
            # class=students[id]["class name"]
            # grades=students[id]["grades"]
            name=cls.students[i_d]["name"]
            grades=cls.students[i_d]["grades"]
            class_name=cls.students[i_d]["class name"]
            student=Students(i_d, name,class_name, grades)
            return student

        return None
    
        
# testing above code
# bob=Students.create("bob", "art", [90,96])
# print(bob.id)
# bob.update_grade([91])
# print(bob.grades)
# print(Students.login(1))
# Students.remove_student(1)
# print(Students.students)
# print (Students.num)