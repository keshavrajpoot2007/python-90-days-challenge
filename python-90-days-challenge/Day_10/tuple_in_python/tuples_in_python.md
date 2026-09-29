# Tuples in Python

A tuple is a collection which is **ordered** and **unchangeable (immutable)**. Tuples are written with round brackets `()`. Because they share many properties with Lists (like indexing and slicing), they are very easy to learn.

## Creating and Accessing Tuples

You can access tuple items using positive or negative indexing, and you can slice them exactly like lists or strings.

```python

anime_names = ("Naruto", "AOT", "Doraemon")

print(anime_names[0])     # Output: Naruto
print(anime_names[-1])    # Output: Doraemon
print(anime_names[::-1])  # Output: ('Doraemon', 'AOT', 'Naruto')

```

## The Defining Feature: Immutability

Unlike lists, you cannot change, add, or remove items once the tuple is created.

```python

# This will throw a TypeError!
anime_names[0] = "One Piece"
# TypeError: 'tuple' object does not support item assignment

```

## Tuple Unpacking

You can extract the values back into separate variables. This is called "unpacking".

```python

cartoon_names = ("Motu Patlu", "Shiva", "Jungle Book")
(var1, var2, var3) = cartoon_names

print(var1) # Output: Motu Patlu

```

*Rule: The number of variables must match the number of values in the tuple, otherwise Python will throw a ValueError.*


## Tuple Operations & Methods

Because tuples are immutable, they don't have `.append()`, `.remove()`, or `.pop()`. They only have two built-in methods:

1. `.count(value)`: Returns the number of times a specified value occurs.

2. `.index(value)`: Searches the tuple for a specified value and returns its position.

You can, however, join two tuples together using the `+` operator. This doesn't modify the existing tuples; it creates a brand new tuple in memory.

## Common Tuple Errors

1. TypeError: Trying to assign a value to an index (tuple[0] = "Value").

2. SyntaxError (Cannot assign to literal): Occurs when you try to unpack into strings instead of variables.
Wrong: `("val1", "val2") = my_tuple`
Correct: `(val1, val2) = my_tuple`

3. AttributeError: Trying to use `.copy()` or list methods like `.append()` on a tuple.

## Key Learning and Interview Points

- Why use Tuples instead of Lists? Tuples are slightly faster and more memory-efficient than lists. They are used to store data that should absolutely not be modified throughout the lifecycle of a program (e.g., Days of the week, database configuration credentials).

- The Missing `.copy()` Method: Tuples don't have a `.copy()` method. Since they are immutable, there is no danger of accidentally modifying them through a reference. Therefore, creating a copy is redundant.

- Single Element Tuple Trap: To create a tuple with only one item, you MUST add a trailing comma ("Motu Patlu",). Without the comma, Python treats it as just a string inside parentheses.