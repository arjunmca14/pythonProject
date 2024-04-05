class Sample:
    collegeName="JNTU"
    def __init__(self):
        self.marks1="marks 1"
        self.marks2="marks 2"
        self.marks3 = "marks 3"

    def myMarks(self):
        print(self.marks1,"::::",self.marks2,":::",self.marks3,":::",self.collegeName)

    def get_marks1(self):
        return self.marks1

    def set_marks1(self,marks1):
        self.marks1=marks1


    def get_marks2(self):
        return self.marks2

    def set_marks2(self,marks2):
        self.marks2=marks2



    def get_marks3(self):
        return self.marks3

    def set_marks3(self,marks3):
        self.marks3=marks3

    def get_Collegename(self):
        return self.collegeName

    def set_collegeName(self,collegeName):
        self.collegeName=collegeName
