# Program 2: Method Overriding (Inheritace based)
class Shape:
    def calculate_area(self):
        pass
    
class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length * self.width
    
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)
        
        
def print_area(shape_object):
    print(f"The area is: {shape_object.calculate_area()}")
    
rect = Rectangle(2, 4)
circle = Circle(4)

print_area(rect)
print_area(circle)