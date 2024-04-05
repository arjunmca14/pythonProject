class College:
    __name="Collge Name"
    __students=[]
    __lecturers=[]

    def __init__(self,name,students=[],lecturers=[]):
        self.__name=name
        self.__students=students
        self.__lecturers=lecturers

    def getName(self):
        return self.__name

    def add_student(self,student):
        self.__students.append(student)


    def add_lecturer(self,lecturer):
        self.__lecturers.append(lecturer)

    def list_students(self):
        for std in self.__students:
            print(std.get_details())


    def list_lecturers(self):
        for lecturer in self.__lecturers:
            print(lecturer.get_details())