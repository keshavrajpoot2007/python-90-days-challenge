a = 10 # Reference count of 10 is 1(a).
b = 10 # Reference count of 10 is 2(a,b).
a = 5 # Reference count of 10 is 1(b) and reference count of 5 is 1(a).
del b # Reference count of 10 is 0 and reference count of 5 is 1(a). So python will delete 10 from memory.

list1 = [1, 2, 3] # Reference count of list1 is 1.
list2 = list1 # Reference count of list1 is 2(list1, list2).
list1 = [4, 5, 6] # Reference count of list1 is 1(list2) and reference count of new list is 1(list1).
list3 = [4, 5, 6] # Reference count of new list [4, 5, 6] is 1(list3) and reference count of list1 is 1(list1), because python will create a new list in memory for list3.