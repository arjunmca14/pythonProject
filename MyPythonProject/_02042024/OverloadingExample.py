from multipledispatch import dispatch


class OverLoad:
    @dispatch(int,int)
    def sumCal(self,a,b):
        return a+b

    @dispatch(int,int,int,int)
    def sumCal(self,a,b,c,d):
        return a+b+c+d
