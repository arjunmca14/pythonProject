class Parent:
    def method1(self):
        print("this is parent method1")
    def method2(self):
        print("this is parent method2")


class Child(Parent):
    def method1(self):
        print("this is child method1>>")

    def method3(self):
        print("this is child method3")