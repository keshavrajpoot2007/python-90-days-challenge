x = 100
y = 100

print(id(x))
print(id(y))
print(x is y)  # True, because both x and y refer to the same integer object in memory

l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(id(l1))
print(id(l2))
print(l1 is l2)  # False, because l1 and l2 are two different list objects in memory, even though they have the same content.