# Alternate numbers pattern using a while loop

# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9

rows = int(input("Enter number of rows: "))
i = 1
j = 1
n = 1
while i <= rows:
    
    while j  <= i:
        print(n, end=" ")
        j += 1
    
    
    n += 2
    j = 1
    i += 1
    print("\n")