def simple_decorator(func):
    def wrapper():
        print("1. Decorator: Before the function runs.")
        func()
        print("3. Decorator: After the function runs.")
    return wrapper

@simple_decorator
def say_hello():
    print("2. Actual Function: Hello, world!")

# Run the program
say_hello()