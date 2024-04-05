from mine.myproject.Person import Person


class Student(Person):
    def __init__(self, name, age, gender, roll_no, course):
        super().__init__(name, age, gender)
        self.roll_no = roll_no
        self.course = course

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Roll No: {self.roll_no}, Course: {self.course}"