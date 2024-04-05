class Student:
    __name__="raju"
    __address__="hyderbad"
    __password__="raju@123"

    def __init__(self,name,address,password):
        self.__name__=name
        self.__address__=address
        self.__password__=password

    def information(self):
        print(self.__name__,":::",self.__address__,"::::",self.__password__)


