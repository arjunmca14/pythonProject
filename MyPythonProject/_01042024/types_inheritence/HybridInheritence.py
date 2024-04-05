class GrandPa:
    def method1(self):
        print("this is method1::grandpa")

class Father(GrandPa):
    def method1(self):
        print("this is method1::Father")


class Mother:
    def method1(self):
        print("this is method1::Mother")


class Child(Father,Mother):
    def method1(self):
        print("this is method1::Child")


c=Child()
c.method1()
print(Child.__mro__)