class Datahiding:
    __password=10
    def getPassword(self):
        return self.__password

    def setPassword(self,p):
        self.__password=p


class Test1(Datahiding):
    def mydata(self):
        print(self.__password)