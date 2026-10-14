'''
Closure - A closure is a function object that has access to variables in its lexical scope, even when the function is called outside that scope. In Python, closures are created by defining a nested function inside an enclosing function and returning the nested function. The nested function can access variables from the enclosing function's scope, even after the enclosing function has finished executing.  
'''

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
# Now closure holds a outer_function with x=10, and inner_function can access x even after outer_function has finished executing.

print(closure(5)) # Output: 15, because the inner_function has access to the variable x from the outer_function's scope, even after the outer_function has finished executing.