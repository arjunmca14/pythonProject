from _02042024.Employee import Employee


class EmployeeUtil:
    def inputData(self):
        id=input("Enter id")
        name=input("Enter name")
        address=input("Enter address")
        salary=input("Enter salary")
        gender=input("Enter gender")

        e = Employee()
        e.setId(id)
        e.setName(name)
        e.setSalary(salary)
        e.setAddress(address)
        e.setGender(gender)
        return e


    def printEmployeeDetails(self,emp):
        print("Employee Details")
        print("======= =========")
        print("id        :",emp.getId())
        print("name      :", emp.getName())
        print("address    :", emp.getAddress())
        print("salary     :", emp.getSalary())
        print("gender     :", emp.getGender())


