from Student import Student


stdlist=[]
while True:
    id=int(input("enter Student id "))
    name=input("enter Student Name ")
    address=input("enter Student Address ")
    marks=int(input("enter Student Marks "))

    s=Student(id,name,address,marks)
    stdlist.append(s)
    choice=input("if you want to continue(Yes/No)")
    if(choice=='no'):
        break



for std in stdlist:
    std.info()
    print("")