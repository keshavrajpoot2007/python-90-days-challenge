class MyClass:
    
    def public_method(self):
        print("This is a public method.")
        
    def _protected_method(self):
        print("This is a protected method.")
        
    def __private_method(self):
        print("This is a private method.")
        

my_object = MyClass()
my_object.public_method()  # Accessible
my_object._protected_method()  # Accessible but not recommended
# my_object.__private_method()  # Not accessible, will raise an AttributeError