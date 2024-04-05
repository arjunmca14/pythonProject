from multipledispatch import dispatch

from project_03042024.Person import Person


class Student(Person):
    __marks=""
    __hallticket=""

    def __init__(self,id,fname,lname,address,contract,gender,email,marks,hallticket):
        super().__init__(id,fname,lname,address,contract,gender,email)
        self.__marks=marks
        self.__hallticket=hallticket



    def getStudentInfo(self):
        self.personInformation()
        print("hallticket   :::", self.__hallticket)
        print("marks   :::",self.__marks)


    def getGenderData(self,gender):
        if  self.__gender==gender:
            print(f"my data complete name:{self.__fname}  {self.__lname} --{self.__marks} ")




