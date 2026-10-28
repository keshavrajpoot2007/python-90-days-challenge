class Samsung:
    def execute(self):
        print("Samsung is a Mobile Company.")

class HP:
    def execute(self):
        print("HP is Laptop Company.")
        
class Jio:
    def execute(self):
        print("Jio is a Network Company.")
        
mobile = Samsung()
laptop = HP()
internet = Jio()

mobile.execute()
laptop.execute()
internet.execute()