from abc import ABC, abstractmethod

from multipledispatch import dispatch


class Person(ABC):
    __id="Person id"
    __fname="Person first name"
    __lname="Person last name"
    __address="Person address"
    __contract="Person contract number"
    __gender="Person gender"
    __email="Person mail id"

    @dispatch(str,str,str,str,str,str,str)
    def __init__(self,id,fname,lname,address,contract,gender,email):
        self.__id=id
        self.__fname=fname
        self.__lname=lname
        self.__address=address
        self.__contract=contract
        self.__gender=gender
        self.__email=email


    @dispatch()
    def __init__(self):
        pass

    def personInformation(self):
        print("id ::",self.__id)
        print("fname:::",self.__fname)
        print("lname:::",self.__lname)
        print("address:::", self.__address)
        print("contract:::", self.__contract)
        print("gender:::", self.__gender)
        print("email:::", self.__email)

    def getGenderData(self,gender):
        if  self.__gender==gender:
            print(f"complete name:{self.__fname}  {self.__lname}  ")



