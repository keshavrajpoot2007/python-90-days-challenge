# Problem: Reverse a string using a loop.

icecream = input("Enter you favourite icecream (eg. vanilla, pista): ").lower()

reversed_icecream = ""

# We done this solution like this because in problem statement it is mentioned that we need to done it using loop. If we want to do it in simple way then we can use slicing method like this: icecream[::-1]

for char in icecream:
    reversed_icecream = char + reversed_icecream

# We can also do it like this, but it is not a good way to do it. It is better to use the above method.
# for i in icecream[::-1]:
#     reversed_icecream += i

print("Reverse order of your icecream is: ", reversed_icecream.capitalize())