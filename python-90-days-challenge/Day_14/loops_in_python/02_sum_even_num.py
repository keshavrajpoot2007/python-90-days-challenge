# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter how many even numbers you want to add: "))
even_sum = 0

for i in range(1, n+1): # Because in python last index is exclusive, thats why weuse n+1.
    
    if i%2 == 0:
        even_sum += i
    
print(f"The sum of {n} even numbers is {even_sum}")
    