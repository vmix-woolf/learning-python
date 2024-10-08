def add(a):
    def add_b(b):
        return a + b
    return add_b

# Використання:
add_5 = add(5)
result = add_5(10)
print(result)
