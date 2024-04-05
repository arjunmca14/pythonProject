class ProtectedAccess:

    def __init__(self):
        self.__name1 = "kartheek"
        self.id = 101

    def method1(self):
        print(self.__name1)
        print(self.id)
class Child1(ProtectedAccess):

    def __init__(self):
        self.id = 111
        self.address = "hyd"


c=Child1()
c.method1()