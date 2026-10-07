# Strings in Python

## Strings

In Python, a string is a sequence of characters enclosed within single quotes, double quotes, or triple quotes. Strings are **immutable**, meaning once created, their elements cannot be changed.

```python

single_quote_str = 'Hello'
double_quote_str = "World"
triple_quote_str = """This is a
multiline string"""

```

## String Indexing and Slicing

Since strings are sequences, you can access individual characters using indexing and multiple characters using slicing. Python supports both positive (left-to-right) and negative (right-to-left) indexing.

- string[index]: Accesses a single character.

- string[start:end]: Accesses a substring from start to end-1.

- string[start:end:step]: Accesses a substring with a specific step.

```python

text = "PythonCode"

# Indexing
print(text[0])       # Output: P
print(text[-1])      # Output: e

# Slicing
print(text[0:6])     # Output: Python
print(text[-4:])     # Output: Code

# Extended Slicing
print(text[::2])     # Output: PtoCd (Skips 1 character)
print(text[::-1])    # Output: edoCnohtyP (Reverses the string)

```

## Basic String Methods

String methods do not modify the original string; they return a new string object in memory.

- .upper(): Converts all characters to uppercase.

- .lower(): Converts all characters to lowercase.

- .strip(): Removes leading and trailing whitespaces.

- .replace(old, new): Replaces all occurrences of a substring with a new one.

```python

anime_character = "   Eren Yeager   "
anime = "Attack on Titan"

print(anime_character.strip())                  # Output: Eren Yeager
print(anime.upper())                  # Output: ATTACK ON TITAN
print(anime_character.replace("Yeager", "Mikasa")) # Output: Eren Mikasa

```

## Splitting and Joining Strings

These methods are used to convert strings to lists and vice versa.

- .split(delimiter): Splits a string into a list of substrings.

- 'delimiter'.join(list): Joins a list of strings into a single string.

```python

# Splitting
heroes = "Ironman, Thor, Hulk"
hero_list = heroes.split(", ")
print(hero_list)  # Output: ['Ironman', 'Thor', 'Hulk']

# Joining
words = ['Python', 'is', 'awesome']
sentence = " ".join(words)
print(sentence)   # Output: Python is awesome

```

## Searching, Counting, and Membership

Python provides built-in methods to search within strings and check for character existence.

- .find(substring): Returns the lowest index of the substring. Returns -1 if not found.

- .count(substring): Returns the number of non-overlapping occurrences.

- len(string): Built-in function that returns the total length of the string.

- in operator: Returns True if a substring exists in the string.

```python

quote = "May the Force be with you"

print(quote.find("Force"))  # Output: 8
print(quote.count("e"))     # Output: 3
print(len(quote))           # Output: 25
print("Force" in quote)     # Output: True

```

## String Formatting

String formatting allows you to dynamically inject variables into strings.

- .format(): Inserts variables into {} placeholders.

- f-strings (Formatted string literals): A modern and faster way to format strings (Python 3.6+).

```python

name = "Keshav"
role = "Developer"

# Using .format()
print("I am {} and I am a {}.".format(name, role))
# Output: I am Keshav and I am a Developer.

# Using f-strings (Industry Standard)
print(f"I am {name} and I am a {role}.")
# Output: I am Keshav and I am a Developer.

```

## Escape Sequences & Raw Strings

Escape characters are used to insert characters that are illegal or have special meaning in a string.

- \n: New line

- \" or \': Escape quotes

- \\: Escape backslash

- r"...": Raw string, ignores all escape sequences.

```python

# Escape Sequence
print("Line1\nLine2")  
# Output: 
# Line1
# Line2

print("He said, \"Hello\"")  # Output: He said, "Hello"

# Raw String (Useful for file paths and regex)
print(r"C:\Users\Keshav\new_folder")  
# Output: C:\Users\Keshav\new_folder

```

## Common String Errors

- IndexError: Occurs when you try to access an index that is out of range (e.g., text[100]).

- TypeError: Occurs when you try to concatenate a string with a non-string without converting it first (e.g., "Age: " + 25).

- AttributeError: Occurs when you try to use a string method on a non-string object, or misspell a method (e.g., text.upeer()).

## Key Learning and Interview Points

- Immutability: Strings in Python cannot be changed after they are created. Operations like .upper() or concatenation create entirely new objects in memory.

- Memory Efficiency: Python uses a mechanism called "String Interning" (String Pool) for small strings, meaning identical strings often point to the same memory address to save space.

- Slicing Safety: Unlike indexing, slicing is forgiving. If you specify an end index out of bounds (e.g., text[0:100]), Python won't throw an IndexError; it will just slice up to the end of the string.

- Join vs Concatenation (+): When combining many strings, using .join() is much faster and more memory-efficient than using the + operator in a loop.