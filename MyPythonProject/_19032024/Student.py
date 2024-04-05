class Student:
    CollegeName="JNTU"
    def __init__(self,id,name,address,marks):
        self.id=id
        self.name=name
        self.address=address
        self.marks=marks

    def findGrade(self):
        grade=""
        if(self.marks>=80 and self.marks<100):
            grade="A Grade"
        elif(self.marks>=60 and self.marks<80):
            grade="B Grade"
        elif(self.marks>=40 and self.marks<60):
            grade="C Grade"
        else:
            grade="D Grade"
        return grade



    def info(self):
        print("ID                 :",self.id)
        print("Name               :", self.name)
        print("Address            :", self.address)
        print("Marks              :", self.marks)
        print("CollegeName        :", Student.CollegeName)
        print("Grade              :",self.findGrade())
