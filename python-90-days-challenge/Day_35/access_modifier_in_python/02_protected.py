class Student:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute
        
class Graduate(Student):
    def display(self):
        print(f"Name: {self._name}, Age: {self._age}")
        
g = Graduate("Alice", 22)
g.display() # Output: Name: Alice, Age: 22