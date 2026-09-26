# Lists in Python

Lists are ordered, mutable (changeable) collections of items. They can store mixed data types and are one of the most heavily used structures in Python.

## List Modification via Indexing & Slicing

Since lists are mutable, you can change their contents directly using indexes.

```python
dramas = ["Hidden Love", "The First Frost", "Love is Sweet"]

# Change single item
dramas[-1] = "Timeless Love"

# Replace multiple items (Replaces 1 item with 2 items)
dramas[1:2] = ["The Early Spring", "Timeless Love"]

# Delete via slicing
dramas[1:3] = []
```

## Common Mistake: String vs List in Slicing

If you assign a string instead of a list to a slice, Python treats the string as an iterable and unpacks every single character as a separate list item.

```python

# What you expected: Replace index 1 with the string
dramas[1:2] = "Neverthless"

# What actually happens:
print(dramas) 
# Output: ['Hidden Love', 'N', 'e', 'v', 'e', 'r', 't', 'h', 'l', 'e', 's', 's', 'Love is Sweet']

```
*Fix: Always assign a list to a slice, like `dramas[1:2] = ["Neverthless"]`.*

## Iteration and Membership

You can easily loop through lists or check if an item exists using `in`.

```python 

dramas = ["Hidden Love", "The First Frost", "Love is Sweet"]

# Loop and print in a single line using end=""
for drama in dramas:
    print(drama, end="-")
# Output: Hidden Love-The First Frost-Love is Sweet-

# Membership Check
if "Hidden Love" in dramas:
    print("Found it!")

```

## Built-in List Methods

- `.append(value)`: Adds an item to the end of the list.

- `.insert(index, value)`: Inserts an item at the specified position.

- `.pop()`: Removes and returns the last item (or the item at a specific index).

- `.remove(value)`: Removes the first matching value (Throws ValueError if not found).

*(Note: There is no `.push()` method in Python lists. We use `.append()` instead.)*

## Memory Assignment vs Copying (Crucial Interview Topic)

When you assign a list to a new variable using `=`, Python does not create a new list. It just creates a new reference pointing to the same memory location. Changing one will change the other.

```python

list_A = ["Apple", "Banana"]
list_B = list_A  # Reference assignment!

list_B.append("Mango")
print(list_A) # Output: ['Apple', 'Banana', 'Mango'] (Original is mutated)

```

**The Solution:** Use `.copy()` to create a shallow copy.

```python

list_A = ["Apple", "Banana"]
list_C = list_A.copy()

print(list_A is list_C) # False (Different memory locations)
print(list_A == list_C) # True (Same values)

```

## List Comprehension

List comprehension provides a concise way to create lists. It replaces standard `for` loops used for generating list items.

```python

# Generating squares of numbers from 0 to 9
squared_num = [x**2 for x in range(10)]

print(squared_num)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```

## Key Learning and Interview Points

- **Mutating slices with sequences:** You can assign a list of size 2 to a slice of size 1 (e.g., list[1:2] = ["A", "B"]). The list automatically expands.

- `is` vs `==`: `==` checks if the values inside two lists are identical. `is` checks if they are the exact same object in memory.

- **Extended Slice Constraint:** If you use a step in slicing (e.g., list[1:4:2]), the sequence you assign to it MUST have the exact same number of elements as the slice. Otherwise, Python throws a ValueError.

