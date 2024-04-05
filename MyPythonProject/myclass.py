class myclass:
    a=20
    b=30

    def mymethod(self):
        print("my a value ",self.a)
        print("my b value ", self.b)



obj=myclass()
print("a value >>>>obj>>",obj.a)
print("b value >>>>obj>>",obj.b)
obj.mymethod()
print("=============================")
obj1=myclass()

obj1.mymethod()

obj1.a=60
obj1.b=50
print("a value >>>>obj1>>",obj1.a)
print("b value >>>>obj1>>",obj1.b)
obj1.mymethod()

obj2=myclass()
obj3=myclass()
obj4=myclass()