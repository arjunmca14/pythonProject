class Person:
    def __init__(self,name,address,salary):

        self.__name=name
        self._address=address
        self.salary=salary

    def information(self):
        print(self.__name,"::",self._address,":::",self.salary)

    def __display(self):
        print("my private data")


# s=Person("raju","hyd",120000)
# s.salary=12000
# s._address="sec"
# s.__name="prakash"
# s.information()
