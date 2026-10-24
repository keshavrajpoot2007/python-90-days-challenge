class Teacher: 
    def __init__(self, name, salary):
        self.name = name # Public attribute
        self.salary = salary # Public attribute
        
t1 = Teacher("John", 50000)
print(t1.name)  # Output: John
t1.name = "Doe"  # Modifying public attribute
print(t1.name)  # Output: Doe