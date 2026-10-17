# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        
    @staticmethod
    def general_description():
        return "Cars are means of transport"
        
    

my_car = Car("Toyota", "Corolla")
print(my_car.general_description())

print(Car.general_description())