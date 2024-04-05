class User:
    name="dummy"
    __password__="dummy@123"
    def displayValues(self):
        print(self.name,":::",self.__password__)