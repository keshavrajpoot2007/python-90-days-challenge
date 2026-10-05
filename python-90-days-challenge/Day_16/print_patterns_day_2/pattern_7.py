# Print reverse number from 10 to 1

# 1
# 3 2
# 6 5 4
# 10 9 8 7

rows = int(input("Enter the number of rows: "))

count = 0

for i in range(1, rows+1):
    sub = count + i
    for j in range(i):
        print(sub, end=" ")
        sub -= 1
        count += 1
    print()

