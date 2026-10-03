# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0

for i in numbers: # Iterate through each number in the list
    if i > 0:
        count += 1 # Increment the count variable by 1 if the number is positive
        

print("The count of positive number is:", count)