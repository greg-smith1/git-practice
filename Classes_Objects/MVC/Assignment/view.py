def prompt_first():
    menu = """
    1) New user? Create Account
    2) Old user? Login
    3) Want to leave? Exit
    Please pick option 1, 2, or 3
    """
    print(menu)
    choice=input("Which option are you picking? ")
    return choice

def prompt_new_user():
    name=str(input("My name is "))
    class_name=str(input("My class name is "))
    return[name, class_name]

def tell_id(student):
    print("Your ID is "+str(student.i_d))
    print("Don't forget your ID, it's very important!")

def prompt_login():
    i_d=input("My student ID is ")
    return int(i_d)

def login_fail():
    print("That ID does not exist! please try again")

def welcome(student):
    print("Welcome "+student.name+"!")

def student_prompt():
    menu = """
    1) Update your grades
    2) Remove your data
    3) View your data
    4) Logout
    Please pick option 1, 2, 3, or 4
    """
    print(menu)
    choice = input('Enter your choice: ')
    return choice

def view_data(student):
    print("Your ID: "+str(student.i_d))
    print("Your Name: "+student.name)
    print("Your Class Name: "+student.class_name)
    print("Your Grades: "+str(student.grades))

def prompt_remove_your_data():
    id_to_remove=int(input("Note: Once you remove this id, when you log out you won't be able to log in with that id again. \n What is the student ID you want to remove? "))
    return id_to_remove

def prompt_update_your_grades():
    grades_to_add=int(input("Enter the grade you want to add to your list of grades: "))
    return grades_to_add

def log_out_screen():
    print("Bye! Come back soon! ")

