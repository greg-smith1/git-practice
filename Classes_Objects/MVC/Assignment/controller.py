from model import Students
import view

def login():
    choice=None
    choice=(view.prompt_first())
    if choice=="1":
        list=view.prompt_new_user()
        student=Students.create(list[0], list[1])
        view.tell_id(student)
        records(student)
    if choice=="2":
        i_d=view.prompt_login()
        student=Students.login(i_d)
        if student != None:
            records(student)
        else:
            view.login_fail()
    if choice=="3":
        view.log_out_screen()
    
    while choice!="3":
        choice=(view.prompt_first())
        if choice=="1":
            list=view.prompt_new_user()
            student=Students.create(list[0], list[1])
            view.tell_id(student)
            records(student)
        if choice=="2":
            i_d=view.prompt_login()
            student=Students.login(i_d)
            if student != None:
                records(student)
            else:
                view.login_fail()


def records(student):
    choice=None
    choice=(view.student_prompt())
    if choice=="1":
        grades_to_add=view.prompt_update_your_grades()
        student.update_grade(grades_to_add)
    if choice=="2":
        id_to_remove=view.prompt_remove_your_data()
        Students.remove_student(id_to_remove)
    if choice=="3":
        view.view_data(student)
    if choice=="4":
        view.log_out_screen()
    while choice!="4":
        choice=(view.student_prompt())
        if choice=="1":
            grades_to_add=view.prompt_update_your_grades()
            student.update_grade(grades_to_add)
        if choice=="2":
            id_to_remove=view.prompt_remove_your_data()
            Students.remove_student(id_to_remove)
        if choice=="3":
            view.view_data(student)


