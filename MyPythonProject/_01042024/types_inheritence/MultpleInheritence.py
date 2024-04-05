class Father:
    def method1(self):
        print("getting the properties...:father")

class Mother:
    def method1(self):
        print("getting some other properties::mother")


class Child(Father,Mother):
    def method2(self):
        print("this is method2")


c=Child()
c.method1()

print(Child.__mro__)