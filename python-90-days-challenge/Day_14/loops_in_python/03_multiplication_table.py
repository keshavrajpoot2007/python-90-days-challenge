# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter the number = "))

for i in range(1, 11):
    if i == 5:
        continue # continue statement is used in python to skip the current iteration of a loop and move on to the next iteration.
    
    print(f"{number} X {i} = {number * i}") # We dont need to write else, because continue skip the iteration. 