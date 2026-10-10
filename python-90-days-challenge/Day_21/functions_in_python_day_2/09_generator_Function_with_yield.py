# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i
        
num = 10
for i in even_generator(num):
    print(i)

