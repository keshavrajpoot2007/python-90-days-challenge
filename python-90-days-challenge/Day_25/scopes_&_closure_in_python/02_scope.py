x  = 99

def func(y):
    z = x + y
    return z

result = func(1)
print(result) # Output: 100, because the variable x is defined in the global scope and can be accessed inside the function func(). The variable y is passed as an argument to the function func() and is local to that function. The variable z is also local to the function func() and is returned as the result of the function.
    
