# Problem: Write a function that takes variable number of arguments and returns their sum.

# def sum_all(*par)  # It works, but it is not a good paractice.

def sum_all(*args): # The asterisk (*) is what gives the unpacking functionality. The name 'args' is standard convention (PEP 8), though any valid identifier works.
    
    return sum(args)

    print(args)  # Prints the tuple: (10, 20, 30). The * in the parameter list packs all positional arguments into a single tuple named args.
    print(*args) # Unpacks the tuple back into individual arguments for print(), outputting: 10 20 30 (without commas or parentheses).
    for i in args:
        print(i * 2)


print(sum_all(10, 20 , 30))