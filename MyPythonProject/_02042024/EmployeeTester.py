from _02042024.Employee import Employee
from _02042024.EmployeeUtil import EmployeeUtil

flag="Y"
while(flag=="y" or flag=="Y"):
    e=EmployeeUtil()
    emp=e.inputData()
    e.printEmployeeDetails(emp)

    flag=input("if you want to continue(Y/N")


