from mine.myproject.College import College
from mine.myproject.Lecturer import Teacher
from mine.myproject.Student import Student


class InputHtmlPage:
    def __init__(self):
        collegeName=input("Please enter Collegename ")
        c=College(collegeName)
        print(c.getName())
        flag="yes"
        while(flag=="yes"):
            print("press 1 :create Student ")
            print("Press 2 : Create lecturer ")
            print("Press 3 : to stop the adding ")
            choice=int(input("Enter your choice"))
            if choice==1:
                print("Student creation")
                student1 = Student("Alice", 20, "Female", "S001", "Computer Science")
                c.add_student(student1)
            elif choice==2:
                print("lecturer creation")
                teacher1 = Teacher("Dr. Smith", 35, "Male", "T001", "Computer Science")
                c.add_lecturer(teacher1)
            elif choice==3:
                flag="no"


        c.list_students()
        c.list_lecturers()

