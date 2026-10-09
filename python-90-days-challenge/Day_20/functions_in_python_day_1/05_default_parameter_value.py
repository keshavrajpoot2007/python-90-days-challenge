# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
def greet(name = "User"):
    return "Hello, " + name + "!"

print(greet())
print(greet("Keshav"))
print(greet())

# Output:-
# Hello, User!
# Hello, Keshav!
# Hello, User!
