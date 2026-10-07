Fruits1 = ["Apple", "Banana", "Mango"]
Fruits2 = Fruits1

print(Fruits1)
print(Fruits2)
print(Fruits1 is Fruits2) #True, because Fruits1 and Fruits2 taking reference of same object.

Fruits1.append("Cherry")

print(Fruits1)
print(Fruits2) # output : ['Apple', 'Banana', 'Mango', 'Cherry'], because Fruits 2 taking the refernce of same object.
