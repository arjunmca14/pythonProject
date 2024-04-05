from Employee1 import Employee1




i=0
while i==0:
    id = input("enter id  ")
    name = input("enter name ")
    address = input("enter address ")
    salary = input("enter salary  ")
    emp = Employee1(id, name, address, salary)
    emp.employeeDetails()
    

    print("u want stop the loop")
    i=int(input("enter your choice(0 or 1)"))