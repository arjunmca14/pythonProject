class Employee1:
    def __init__(self,id1,name,address,salary):
        self.id=id1
        self.name=name
        self.address=address
        self.salary=salary

    def employeeDetails(self):
        print(self.id ,":::",self.name+":::",self.address,":::",self.salary)