from _02042024.OverRidingExample import Parent, Child

p=Parent()
p.method1()
p.method2()
print("===================")
c=Child()
c.method1(100)  #child
c.method2()  #parent
c.method3()  #child