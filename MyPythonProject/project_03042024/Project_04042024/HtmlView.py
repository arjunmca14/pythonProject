from project_03042024.Lecturer import Lecturer
from project_03042024.Project_04042024.College import College
from project_03042024.Student import Student


class htmlPages:

    def registrationHtmlPage(self):
        collgeName=input("Please enter College name ")
        self.c=College(collgeName)

        print("College NAme is :::",self.c.getCollegeName())

        flag="Y"
        while flag=="y" or flag=="Y":
            print("===================================")
            print("Press 1 : Student registration")
            print("press 2 : lecturer registration")
            print("Press 3 : exit")


            choice=input("enter your choice")
            if choice=="1":
                print("Student registration started")
                id=input("Enter student id")
                fname=input("Enter student first name")
                lname = input("Enter student last name")
                address = input("Enter student address")
                contract = input("Enter student constract")
                gender = input("Enter student gender")
                email = input("Enter student email")
                marks = input("Enter student marks")
                hallticket = input("Enter student hallticket")
                s = Student(id,fname,lname,address,contract,gender,email,marks,hallticket)
                self.c.add_Student(s)

            elif choice=="2":
                print("Lecturer registraion started")
                l = Lecturer("101", "raju", "r", "hyd", "900018", "Male", "raju@gmail.com", "12000")
                self.c.add_lecturer(l)

            else:
                flag=input("If you want to continue(Y/N)")


    def displayAllDetails(self):

        print("Press 1 : student information")
        print("Press 2 : lecturer information")
        print("press 3 : exist")
        choice=input("Enter your choice")
        if choice=="1":
            self.c.display_StudentData()
        elif choice=="2":
            self.c.display_LecturerData()
        else:
            print("exist the menu")


    def basedonGenderNeedtoGetData(self):
        print("Press 1 : student information based on gender")
        print("Press 2 : lecturer information based on gender")
        print("press 3 : exist")
        choice = input("Enter your choice")
        if choice == "1":
            gender=input("please enter student gender for filter")
            self.c.display_StudentDataBasedonGender(gender)
        elif choice == "2":
            gender = input("please enter lecturer gender for filter")
            self.c.display_LecturerDataBasedonGender(gender)
        else:
            print("exist the menu")