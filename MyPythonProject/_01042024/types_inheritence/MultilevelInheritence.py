class GrandPa:
    def method1(self):
        print("this is Grandpa Method1")

class Parent(GrandPa):
    def method1(self):
        print("this is Parent Method1")


class Child(Parent):
    def method2(self):
        print("this is Child Method2")




c=Child()
c.method1()
print(Child.__mro__)