class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"
    
    def __repr__(self):
        return f"Object Human (\n" \
            f"    name={self.name},\n" \
            f"    age={self.age}\n" \
        f")"

human = Human("Alice", 30)
print(human)
print(repr(human))
