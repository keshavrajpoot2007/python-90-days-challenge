# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.__model = model
        
    @property
    def model(self):
        return self.__model
        
    
my_car = Car("Toyota", "Corolla")

print(my_car.model)

# my_car.model = "City"   # AttributeError: property 'model of 'Car' obhect has no setter
# print(my_car.model)