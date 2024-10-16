class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

point = Point(2, 3)
print(repr(point))  # Виводить: Point(x=2, y=3)


new_point = eval(repr(point))
print(new_point)
print(id(point))
print(id(new_point))
