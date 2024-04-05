class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Student(Person):
    def __init__(self, name, age, gender, roll_no, course):
        super().__init__(name, age, gender)
        self.roll_no = roll_no
        self.course = course

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Roll No: {self.roll_no}, Course: {self.course}"


class Teacher(Person):
    def __init__(self, name, age, gender, emp_id, subject):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.subject = subject

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Employee ID: {self.emp_id}, Subject: {self.subject}"


class College:
    def __init__(self, name, students=None, teachers=None):
        self.name = name
        self.students = students if students else []
        self.teachers = teachers if teachers else []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def list_students(self):
        print("Students in", self.name)
        for student in self.students:
            print(student.get_details())

    def list_teachers(self):
        print("Teachers in", self.name)
        for teacher in self.teachers:
            print(teacher.get_details())


# Sample usage
if __name__ == "__main__":
    # Creating students and teachers
    student1 = Student("Alice", 20, "Female", "S001", "Computer Science")
    student2 = Student("Bob", 21, "Male", "S002", "Mathematics")

    teacher1 = Teacher("Dr. Smith", 35, "Male", "T001", "Computer Science")
    teacher2 = Teacher("Prof. Johnson", 40, "Female", "T002", "Mathematics")

    # Creating college
    college = College("ABC College")

    # Adding students and teachers to the college
    college.add_student(student1)
    college.add_student(student2)

    college.add_teacher(teacher1)
    college.add_teacher(teacher2)

    # Listing students and teachers
    college.list_students()
    print()
    college.list_teachers()
