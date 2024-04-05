class publicAccess:
    name='raju'
    def __init__(self):
        self.name="kartheek"
        self.id=101




class Child(publicAccess):
    def __init__(self):
        self.name="phani"
        self.id=111
        self.address="hyd"

