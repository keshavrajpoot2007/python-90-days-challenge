x = 99
y = 100

def func():
    x = 88
    global y
    y = 200
    
    '''
    Note: Avoid using global variables and rewriting them inside functions, as it can lead to unexpected behavior and make the code harder to understand and maintain. Instead, consider passing variables as arguments to functions or returning values from functions to update variables in the global scope.
    '''
    
func()

print(x) # Output: 99, because the variable x defined inside the function func() is local to that function and does not affect the global variable x.

print(y) # Output: 200, because the variable y is declared as global inside the function func() and its value is modified within that function.