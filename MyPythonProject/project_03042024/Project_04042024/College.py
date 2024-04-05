class College:
    __name=""
    __students=[]
    __lecturers=[]

    def __init__(self,name,students=[],lecturers=[]):
        self.__name=name
        self.__students=students
        self.__lecturers=lecturers

    def getCollegeName(self):
        return self.__name


    def add_Student(self,student):
        self.__students.append(student)


    def add_lecturer(self,lecturer):
        self.__lecturers.append(lecturer)


    def display_StudentData(self):
        for std in self.__students:
            std.getStudentInfo()
            print("-------------------------------------------------")

    def display_LecturerData(self):
        for lecturer in self.__lecturers:
            lecturer.getLecturerInfo()
            print("-----------------------------------------------")




    def display_StudentDataBasedonGender(self,gender):
        for std in self.__students:
            std.getGenderData(gender)
            print("-------------------------------------------------")

    def display_LecturerDataBasedonGender(self, gender):
         for lec in self.__lecturers:
             lec.getGenderData(gender)
             print("-------------------------------------------------")

