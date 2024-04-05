class Employee:
    __id="id"
    __name="name"
    __address="address"
    __salary="salary"
    __gender="gender"

    def setId(self,id):
        self.__id=id

    def getId(self):
        return self.__id

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setAddress(self,address):
        self.__address=address
    def getAddress(self):
        return self.__address


    def setSalary(self,salary):
        self.__salary=salary
    def getSalary(self):
        return self.__salary


    def setGender(self,gender):
        self.__gender=gender
    def getGender(self):
        return self.__gender

    #
    # def __init__(self,id,name,address,salary,gender):
    #     self.__id=id
    #     self.__name=name
    #     self.__address=address
    #     self.__salary=salary
    #     self.__gender=gender

    def __int__(self):
        pass