'''
Scopes - Scopes are the regions of a program where a namespace is directly accessible. In Python, there are four types of scopes:
1. Local Scope: The innermost scope, which is searched first, contains the local names. This scope is created when a function is called, and lasts until the function returns.
2. Enclosing Scope: The scope of any enclosing functions, which are searched next, contains the nonlocal, but also non-global names. This is applicable only to nested functions.
3. Global Scope: The scope of the module, which is searched next, contains the global names. This scope lasts until the script ends.
4. Built-in Scope: The outermost scope, which is searched last, contains the built-in names. This scope is created when the Python interpreter starts up, and is never deleted.
'''


username = "Keshav Rajpoot"
nickname = "KV"

def func():
    # nickname = "Keshav" 
    print(nickname) # Output: KV, because function func() cant find the variable nickname defined inside the function func() and it will look for the variable nickname in the global scope.
    
    username = "Keshav"
    print(username) # Output: Keshav, because the variable username defined inside the function func() is local to that function.
    

print(username) # Output: Keshav Rajpoot, because the variable username defined inside the function func() is local to that function and does not affect the global variable username.

func() # Output: Keshav, because the variable username defined inside the function func() is local to that function.