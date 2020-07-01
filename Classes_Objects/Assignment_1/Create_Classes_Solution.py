class Person:
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

class Student(Person):
    def __init__(self, first_name, last_name, gpa, classes):
        self.first_name=first_name
        self.last_name=last_name
        self.gpa=gpa
        self.classes=classes
    def update_gpa(self, gpa):
        self.gpa=gpa

class Teacher(Person):
    def __init__(self, first_name, last_name, tenure, subject):
        self.first_name=first_name
        self.last_name=last_name
        self.tenure=tenure
        self.subject=subject

    def create_students(self, list_of_students):
        self.students=[]
        self.students.append(list_of_students)

# testing above code:
# bob=Student("bob", "l.", 3.0, ["math", "english"])
# randy=Student("randy", "s.", 4.0, ["cs", "art"])
# print (bob.gpa)
# randy.update_gpa(3.5)
# print (randy.gpa)
# lily=Teacher("lily", "h.", True, "history")
# lily.create_students([bob, randy])


class Food:
    def __init__(self, name, healthy, price):
        self.name=name
        self.healthy=healthy
        self.price=price

class ShoppingList:
    def __init__(self, shopping_list=[]):
        self.shopping_list=shopping_list

    def add_to_list(self,name, healthy, price):
        food_instance=Food(name, healthy, price)
        self.shopping_list.append(food_instance)

    def view_list(self):
        total=0
        for i in self.shopping_list:
            total+=i.price
            print(i.name, i.price)
        print("total price: "+str(total))

# testing above code
# broc=Food("broccoli",True, 3.0)
# print(broc.healthy)
# l=ShoppingList([broc])
# l.add_to_list("crackers", False, 5.0)
# l.view_list()
