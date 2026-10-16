# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    
    total_car = 0
    
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    
my_car = Car("Toyota", "Corolla")
Car("Tata", "Nexon")

print(Car.total_car)