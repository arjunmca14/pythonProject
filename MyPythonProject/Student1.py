class Student1:
    collegeName=""

    def __init__(self):
        self.id=101
        self.name="raju"
        self.marks=78


    def mydata(self):
        print("  id    ",self.id)
        print("name  ",self.name)
        print("marks    ",self.marks)
        print("collegeName  ",Student1.collegeName)
