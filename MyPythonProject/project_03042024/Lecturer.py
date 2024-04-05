from project_03042024.Person import Person


class Lecturer(Person):
    __salary=""

    def __init__(self,id,fname,lname,address,contract,gender,email,salary):
        super().__init__(id,fname,lname,address,contract,gender,email)
        self.__salary=salary




    def getLecturerInfo(self):
        self.personInformation()
        print("Salary   :::", self.__salary)

