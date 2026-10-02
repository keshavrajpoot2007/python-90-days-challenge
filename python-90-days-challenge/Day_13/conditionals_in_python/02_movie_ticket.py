# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

import random

age = int(input("Enter Your age: "))
day = random.choice(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']) 

price = 12 if age >= 18 else 8 # Python also allow to write conditions in this way.

if day == 'Wednesday':
    price -= 2 # You can also write price = price - 2, both are same in every way.
    
print(f"Today is {day}, and you are {age} year old, so ticket price for you is ${price}")