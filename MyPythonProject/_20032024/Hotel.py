class Hotel:
    def __init__(self):
        self.food=[]

        self.price=0.0

    def orderItem(self,item):
        self.food.append(item)

    def myItems(self):
        for item in self.food:
            data=item.split(' ')
            print(item)

    def menuWithPrice(self,food):
        if(food=='dosa'):
            self.price=20
        elif(food=='idly'):
            self.price=10
        elif(food=='pongal'):
            self.price=20
        return self.price

    def totalPrice(self):
        sum=0.0
        for item in self.food:
            data = item.split(' ')
            temp=int(data[0])*int(self.menuWithPrice(data[1]))
            sum=sum+int(temp)

        return sum

    def bill(self):
        print("==============")
        print("Bill Details")
        print("==============")
        for item in self.food:
            data = item.split(' ')
            temp = int(data[0]) * int(self.menuWithPrice(data[1]))
            print(item,' : price:  ',temp)
        print("----------------")
        print("total bill: ",self.totalPrice())
