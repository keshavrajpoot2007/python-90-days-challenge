x = 99 
y = 100

def f1():
    x = 88
    
    def f2():
        print(x) # Output: 88, because the variable x defined in the enclosing function f1() is accessible inside the nested function f2() due to the concept of closures in Python.
        print(y) # Output: 100, because the variable y is accessible inside the nested function f2() due to the concept of closures in Python.
        
        # It is called climbing the scope chain, where the nested function f2() can access variables from its enclosing function f1() and the global scope.
    f2()
    return f2

        
f1()
myresult = f1()

myresult() # Output: 88, because the variable x defined in the enclosing function f1() is accessible inside the nested function f2() due to the concept of closures in Python.

# It is called closures, where the nested function f2() retains access to the variables of its enclosing function f1() even after f1() has finished executing.

