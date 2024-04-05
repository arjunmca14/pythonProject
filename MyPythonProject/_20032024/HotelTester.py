from _20032024.Hotel import Hotel

h=Hotel()
h.orderItem('6 idly')
h.orderItem('4 dosa')

h.myItems()
price=h.totalPrice()
print("total price ",price)
h.bill()