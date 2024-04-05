class Parent:
    def method1(self):
        print("this is method1::Parent")

class Child1(Parent):
    def method1(self):
        print("this is method1::Child1")

    def method3(self):
        print("this is method3::Child1")
class Child2(Parent):
    def method1(self):
        print("this is method1::Child2")

    def method2(self):
        print("this is method2::Child2")


c=Child1()
c.method1()
c.method3()
# c.method2()