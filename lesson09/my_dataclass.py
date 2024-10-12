from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height

rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

print(f"Площа прямокутника 1: {rect1.area()}")
print(f"Площа прямокутника 2: {rect2.area()}")
print(f"Площа прямокутника 3: {rect3.area()}")
