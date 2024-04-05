class Student:
    name="raju"
    __password="raju@123"

    def mydata(self):
        print(self.__password)





s=Student()
print(s.name)
# print(s.__password)
s.mydata()