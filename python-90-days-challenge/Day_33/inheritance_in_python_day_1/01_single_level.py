# Single level Inheritance in Python

'''
Single level inheritance is a type of inheritance where a child class inherits from a single parent class. In this example, the `Programmer` class inherits from the `Employee` class, allowing it to access the methods and attributes of the `Employee` class while also having its own unique methods.
'''


class Employee:
    
    def __init__(self, name, id):
         self.name = name
         self.id = id
         
    def showdetails(self):
        print(f"The Employee name is {self.name} and id is {self.id}.")
        

class Programmer(Employee): 
    
    def showlanguage(self):
        print("The language is Python.")
        
e = Employee('Luke', 30)
e.showdetails() # Ouput: The Employee name is Luke and id is 30.

p = Programmer('Flora', 25)
p.showdetails() # Ouput: The Employee name is Flora and id is 25.
p.showlanguage() # Ouput: The language is Python.