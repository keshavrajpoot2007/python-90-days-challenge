# Another reverse number pattern

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

rows = int(input("Enter number of rows: "))
# temp = rows
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=" ")
        
    # temp -= 1
    print("")
    