# Square pattern with numbers

# 1 2 3 4 5 
# 2 2 3 4 5 
# 3 3 3 4 5 
# 4 4 4 4 5 
# 5 5 5 5 5

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, rows+1):
        if j <= i:
            print(i, end=" ")
        else:
            print(j, end=" ")
            
    print()