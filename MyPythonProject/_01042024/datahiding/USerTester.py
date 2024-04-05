from _01042024.datahiding.User import User

u=User()
u.displayValues()

# change the name and password
u.name="raju"
u.__password__="raju@123"
u.displayValues()
