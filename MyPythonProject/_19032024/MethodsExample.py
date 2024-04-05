class MethodExample:
    name="sample"
    def __init__(self):
        print("default constructor")

    def m1(self):
        print("instance method")

    @classmethod
    def classMethod(cls):
        print(cls.name)

    @staticmethod
    def mymethod():
        print("static method")
