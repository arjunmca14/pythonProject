from _01042024.AccessModifiers.PublicAccessModifier import Parent, Child

p=Parent()
print(p.name)
p.name="rakesh"
print(p.name)


c=Child()
print(c.name,"::",c.age)
c.name="keerthi"
c.age=34
print(c.name,"::",c.age)