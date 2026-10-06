# Pascal’s triangle pattern using numbers

# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
# 1 5 10 10 5 1 
# 1 6 15 20 15 6 1

row = int(input("Enter the number of rows: "))


temp_list = [1]

for i in range(1, row + 1):
    
    main_list = [0] + temp_list + [0]
    temp_list = []
    # main_list.append(i)
    for j in range(0,i):
        next = main_list[j] + main_list[j+1]
        print(next, end=" ")
        temp_list.append(next)
    
    print()
        
        
        
        
