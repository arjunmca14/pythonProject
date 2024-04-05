from mine.AllAccessModifierExample import Person

a=Person("raju","hyd",12000)
a.information()
a.salary=10000

a._address="sec"
a.information()
print(a.__name)
a.information()
a.__display()