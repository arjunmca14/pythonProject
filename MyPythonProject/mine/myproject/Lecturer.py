from mine.myproject.Person import Person


class Teacher(Person):
    def __init__(self, name, age, gender, emp_id, subject):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.subject = subject

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Employee ID: {self.emp_id}, Subject: {self.subject}"

