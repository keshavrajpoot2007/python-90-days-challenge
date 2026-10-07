# Day 1: Memory Management & Variables in Python
**Author:** Keshav Rajpoot
**Repository:** Python The Ultimate World

## Definition
In Python, variables do not act as static memory containers or blocks (as they do in C or Java). Instead, they act as dynamic "references" or "name tags" that point to data objects stored in the heap memory. 

## Advantage
This reference-based system provides automatic memory optimization. If multiple variables are assigned the same immutable value (e.g., `x = 100` and `y = 100`), Python allocates the object `100` only once in memory and points both variables to the exact same address, significantly reducing memory consumption.

## Disadvantage
The primary drawback occurs when working with mutable objects (like Lists or Dictionaries). If two variables reference the same list, modifying the data through one variable (e.g., `list2.append(3)`) will unintentionally alter the data for the other variable as well. This shared state often leads to hidden, unexpected bugs for developers transitioning from other languages.

## Working
Python handles this object reference system dynamically at runtime through specific mechanisms:

*   **Memory Address:** The `id()` function returns the exact memory address (identity) of the object a variable is pointing to.

*   **Identity vs. Equality:** The `==` operator evaluates if the *values* of two objects are equal, whereas the `is` operator evaluates if two variables point to the exact same *memory location*.

*   **Garbage Collection:** When a data object loses all its variable references (e.g., the variables are reassigned or deleted), Python's Garbage Collector automatically identifies the unused data and deletes it from memory to free up space.

### Practical Implementation
```python
// Program by Keshav Rajpoot
print("Name = Keshav Rajpoot \n")

# Memory reference test for immutable objects
x = 100
y = 100

print(f"Memory Address of x: {id(x)}")
print(f"Memory Address of y: {id(y)}")
# Checking if both variables point to the exact same location
print(f"Are x and y exactly the same object? {x is y}")
```
