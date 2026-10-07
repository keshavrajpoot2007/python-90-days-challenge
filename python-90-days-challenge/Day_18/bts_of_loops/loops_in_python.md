# Loops in Python

Loops are used to execute a block of code repeatedly until a certain condition is met. Python provides two main types of loops: `for` loops and `while` loops.

## `for` 

`for` loops are used for iterating over a sequence (like a list, tuple, dictionary, set, or string). This is less like the `for` keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

```python

for item in [1, 2, 3, 4, 5]:
    print(item)

```

## `while`

`while` loops execute a block of code as long as a specified condition is true. 

```python
count = 0
while count < 5:
    print(count)
    count += 1  

```

## Loop Control Statements

- `break`: Exits the loop immediately.
- `continue`: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
- `pass`: Does nothing, acts as a placeholder.
- `else`: Can be used with loops. The `else` block will execute after the loop finishes normally (without hitting a `break`).

```python
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
    elif i == 2:
        continue  # Skip the rest of the code when i is 2
    elif i == 1:
        pass  # Do nothing when i is 1
    else:
        print("This will not be printed when i is 2 or 3")
else:
    print("Loop finished normally") 

```

## Iterators and Iterables

An **iterator** is an object that contains a countable number of values. An iterator is an object that can be iterated upon, meaning you can traverse through all the values.

An **iterable** is any object in Python that can be looped over. Examples of iterables include lists, tuples, dictionaries, sets, and strings.

## Iterator tools

In Python, you can create an iterator from an iterable using the `iter()` function. You can then retrieve the next item from the iterator using the `next()` function.

```python
my_list = [1, 2, 3]     
I = iter(my_list)  # Create an iterator from the list
print(next(I))  # Output: 1
print(next(I))  # Output: 2
print(next(I))  # Output: 3
print(next(I))  # Raises StopIteration exception    
```

## Iterable objects and their iterators

Iterable objects are those that can be looped over, while their iterators are the objects that actually perform the iteration. When you use a `for` loop on an iterable, Python automatically calls the `iter()` function to create an iterator and then repeatedly calls `next()` to retrieve each item.

```python
my_list = [1, 2, 3]
for item in my_list:
    print(item)
```

In this example, `my_list` is an iterable, and Python creates an iterator behind the scenes to handle the iteration.

## Key Learning and Interview Points

1. Iterable vs. Iterator (The Core Difference)

- Iterable: An object you can loop over (like a List, String, or Tuple). It contains data but doesn't remember its current state during a loop.

- Iterator: An object that remembers its state and produces the next value in the sequence when `next()` is called.

2. The Tricky Output Question (`iter(x) is x`)

- `iter(list) is list` -> False. Lists are iterables, but not iterators. Calling `iter()` on a list creates a brand new, separate iterator object in memory.

- `iter(file) is file` -> True. File objects are their own iterators. They maintain their own internal cursor state.

3. How a `for` Loop Actually Works (Under the Hood)
When you write `for item in data:`, Python internally does three things:

- Calls `iter(data)` to create an iterator object.

- Continuously calls `next()` on that iterator to fetch items one by one.

- Silently catches the `StopIteration` exception to gracefully end the loop without crashing the program.

4. Reaching the End of Data (`readline()` vs `__next__()`)

- If you use a file's `.readline()` method, it returns an empty string (`""`) when the file ends.

- If you use the iterator method `.__next__()` (or `next()`), it raises a `StopIteration` exception when there are no items left.

5. The Iterator Protocol (Dunder Methods)
For any object in Python to work inside a for loop, it must implement the Iterator Protocol, which consists of two built-in dunder (double underscore) methods: `__iter__()` and `__next__()`.
