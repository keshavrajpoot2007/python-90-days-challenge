class Geek:
    def __init__(self, name, roll, branch):
        self.__name = name # private member
        self.__roll = roll # private member
        self.__branch = branch # private member
        
    def __displayDetails(self): # private method
        print(f"Name: {self.__name}, Roll: {self.__roll}, Branch: {self.__branch}")

    def accessPrivateFunction(self):
        self.__displayDetails()

g = Geek("R2J", 1706256, "IT")
g.accessPrivateFunction()
# Output:
# Name: R2J
# Roll: 1706256
# Branch: IT
