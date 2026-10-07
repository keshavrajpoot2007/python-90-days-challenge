p = 500
q = p
print(id(p))
print(id(q))

#Que. Here, is there new object of 500 is created for q by writing q = p, or it is pointing the
#     same object?

#Ans. q is pointing the same object, because in python check in memory that which object p is pointing
#     and copies it in q.