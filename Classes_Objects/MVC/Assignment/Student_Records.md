## Student Records System

Let's make a student records system, separated into a Model, View and Controller. As in lecture, the Model and View should not communicate with each other in any way, and the Controller should handle function calls and deciding which logic is executed by the program.  

Our system should:  
* Let a user log in (we need to know who's using the system and if they're authorized)
* Let a user create an account
* Add new students
* Update a student's grades
* Remove a student from the data
* View a student

Each student should have:
* A name
* Grades (a list)
* A class name (the current class they're enrolled in, a string)
* A unique ID, since name may technically not be unique  

Users should not be able to perform any actions (other than logging in or creating a new accout) until they have logged in successfully. The application should start up via the `run.py` file.
