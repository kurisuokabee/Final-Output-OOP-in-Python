class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Using duck typing in __add__
    def __add__(self, other):
        try:
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)
        except AttributeError:
            raise TypeError("The object passed does not have x and y attributes")

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


v1 = Vector(1, 2)
p1 = Point(3, 4)

v2 = v1 + p1 
print(v2)     # Output: Vector(4, 6)
