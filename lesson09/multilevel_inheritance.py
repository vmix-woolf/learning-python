class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())  # Виведе порядок розв'язання методів для класу D
print(D.__mro__)
