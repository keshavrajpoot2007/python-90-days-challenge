num = input("Enter 10: ")
print(num*2)

#Que. When we enter 10, then what output will come 20 or 1010? What understanding we get about
#     the property of object created by input() function?

#Ans. The output we get is 1010, because input always take string, we need to convert it into int
#     if we want 20. When we run this program and python interpreted come to line 1, where we write
#     num = input("Enter 10: "), it take pause and ask user for input then it created the object of 
#     our input and create num in dictionary and give refernce of our input object to num.