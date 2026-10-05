# Number triangle pattern

#           1 
#         1 2 
#       1 2 3 
#     1 2 3 4 
#   1 2 3 4 5 



# <-----------------------1st method----------------------->
rows = int(input("Enter number of rows: "))
temp = 1
for i in range(rows,0,-1):
    for j in range(i+1):
        print(" ", end=" ")
        
    for k in range(1, temp+1):
        print(k, end=" ")
        
    temp += 1
    print()

# <-----------------------2nd method----------------------->

# rows = 6
# for i in range(1, rows+1):
#     num = 1
#     for j in range(rows, 0, -1):
#         if j > i:
#             print(" ", end=' ')
#         else:
#             print(num, end=' ')
#             num += 1
#     print("")