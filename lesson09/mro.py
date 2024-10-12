class A:
    name = "Я клас A"

class B:
    name = "Я клас B"
    property = "Я знаходжусь в класі B"

class C(B, A):
    property = "Я знаходжусь в класі C"

c = C()
print(c.name)
print(c.property)
print(C.__mro__)
