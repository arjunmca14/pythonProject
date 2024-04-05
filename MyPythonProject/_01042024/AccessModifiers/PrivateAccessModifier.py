class Parent:
    __name__="raju"

    def method1(self):
        print(self.__name__)

class Child(Parent):

    def method2(self):
        print(self.__name__)