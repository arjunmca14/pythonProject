import multipledispatch
from multipledispatch import dispatch
# pip3 install multipledispatch
class Overload:
    @multipledispatch.dispatch(int,int)
    def add(self,a,b):
        return a+b

    @multipledispatch.dispatch(int, int,int)
    def add(self,a,b,c):
        return  a+b+c


o=Overload()
print(o.add(10,20,3))
print(o.add(10,20))