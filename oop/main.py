class  Point:
    def __init__(self):
        self.y = None
        self.x = None

    def reset(self):
        self.x = 0
        self.y = 0


p = Point()
p.reset()
print(p.x, p.y)

