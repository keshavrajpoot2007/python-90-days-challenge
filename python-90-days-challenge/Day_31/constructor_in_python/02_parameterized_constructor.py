class Employee:
    
    # If a constructor is defined with multiple parameters along with self is called as parameterized constructor.
    def __init__(self, name, age ):
        self.name = name
        self.age = age
        
emp1 = Employee('James', 20)
emp2 = Employee('Badie', 22)

print("Name =", emp1.name)
print("Age =", emp1.age)
print("Name =", emp2.name)
print("Age =", emp2.age)
        
        