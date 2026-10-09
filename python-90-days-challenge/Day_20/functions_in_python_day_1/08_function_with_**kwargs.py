# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):
     
     for key, value in kwargs.items():
         print(f"{key}: {value}")
         
print_kwargs(name = "Keshav", gender = "Male")
print_kwargs(name = "Keshav")
print_kwargs(a = 2, b = 3, c = 4, d = 5)