a = 10
print(id(a))
a = 15
print(id(a))

#Que. if number is immutable, then why the address if is changed

#Ans. Because the value of object 10 is not changed in memory, infact the new object 15 is created, 
#     and variable a is taking reference from second object 15 instead of object 10,thats why it 
#     is immutable because 10 is never changed, it is handeled by garbage collector when it have no
#     use.