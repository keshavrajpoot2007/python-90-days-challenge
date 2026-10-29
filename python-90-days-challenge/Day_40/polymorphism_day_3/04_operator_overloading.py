class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
        
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(2, 3)
v2 = Vector(5, 7)

v3 = v1 + v2
print(v1)
print(v3)
