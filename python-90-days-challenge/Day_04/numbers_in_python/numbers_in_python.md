# Numbers in Python

Python supports several types of numbers:

1. **Integers (int)**: Whole numbers without a decimal point.
2. **Floating-point numbers (float)**: Numbers with a decimal point.
3. **Complex numbers (complex)**: Numbers with a real and imaginary part.

## Integer Operations

Integers in Python can be positive or negative, and they have unlimited precision.

```python
x = 5
y = -10
z = 0
```

## Floating-point Operations

Floating-point numbers are used to represent real numbers.

```python
x = 3.14
y = -2.5
z = 0.0
```

## Complex Number Operations

Complex numbers have a real and an imaginary part.

```python
x = 3 + 4j
y = 2 - 1j
```

## Type Conversion

You can convert between different number types using built-in functions:

- `int()`: Converts to an integer.
- `float()`: Converts to a floating-point number.
- `complex()`: Converts to a complex number.

```python
x = int(3.14)  # x is now 3
y = float(5)   # y is now 5.0
z = complex(3, 4)  # z is now (3+4j)
```

## Arithmetic Operations

Python supports the following arithmetic operations:

- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division (returns a float)
- `//`: Floor division (returns an integer)
- `%`: Modulus (returns the remainder)
- `**`: Exponentiation
- `<<`: Left shift
- `>>`: Right shift

```python
a = 10
b = 3

print(a + b)   # Output: 13
print(a - b)   # Output: 7
print(a * b)   # Output: 30
print(a / b)   # Output: 3.3333333333333335
print(a // b)  # Output: 3
print(a % b)   # Output: 1
print(a ** b)  # Output: 1000
```

## Logical Operations

Python supports the following logical operations:

- `and`: Returns True if both statements are true.
- `or`: Returns True if at least one statement is true.
- `not`: Returns True if the statement is false.

```python
x = True
y = False
z = not x  # z is now False
True and False  # Output: False
True or False   # Output: True
not x           # Output: False

a = True + 3  # Output: 4, because True is treated as 1 in arithmetic operations
True is 1  # Output: False, because True is a boolean, not an integer

``` 

## Numbers Error

- ValueError occurs when a function receives an argument of the right type but an inappropriate value.

- TypeError occurs when a function receives an argument of the wrong type.

- ZeroDivisionError occurs when a number is divided by zero.

- OverflowError occurs when a calculation exceeds the maximum limit for a numeric type.

- FloatingPointError occurs when a floating-point operation fails.


# Base Conversion

- Python supports different number bases:

    - Binary (base 2): Numbers prefixed with `0b`
    - Octal (base 8): Numbers prefixed with `0o`
    - Hexadecimal (base 16): Numbers prefixed with `0x`
    - Decimal (base 10): Standard numbers without any prefix

- You can convert between these bases using built-in functions:

    - `bin()`: Converts an integer to a binary string.
    - `oct()`: Converts an integer to an octal string.
    - `hex()`: Converts an integer to a hexadecimal string.
    - `int()`: Converts a string in a given base to an integer.

```python
x = 10
print(bin(x))  # Output: 0b1010
print(oct(x))  # Output: 0o12
print(hex(x))  # Output: 0xa

print(int('1010', 2))  # Output: 10
print(int('12', 8))    # Output: 10
print(int('a', 16))    # Output: 10

print(0b1010)  # Output: 10
print(0o12)    # Output: 10
print(0xa)     # Output: 10

```

## Floating Point Precision vs Decimal Precision

- Floating-point numbers in Python are represented using the IEEE 754 double-precision format, which provides about 15-17 decimal digits of precision. This can lead to small rounding errors in calculations.

- The `decimal` module in Python provides a `Decimal` class that allows for exact decimal arithmetic, which is useful for financial and monetary calculations where precision is critical.

```python
x = 0.1 + 0.1 + 0.1 - 0.3
print(x)  # Output: 5.551115123125783e-17 (not exactly zero due to floating-point precision)

from decimal import Decimal
y = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') #Always use string representation to avoid floating-point issues.
print(y)  # Output: 0. Because Decimal provides exact decimal arithmetic, the result is exactly zero.
```

## Built-in Functions for Numbers

Python provides several built-in functions for working with numbers:

- `abs()`: Returns the absolute value of a number.
- `round()`: Rounds a floating-point number to a specified number of decimal places.
- `max()`: Returns the largest item in an iterable or the largest of two or more arguments.
- `min()`: Returns the smallest item in an iterable or the smallest of two or more arguments.
- `sum()`: Returns the sum of all items in an iterable.

```python
x = -5
y = 3.14159
z = [1, 2, 3, 4, 5]

print(abs(x))     # Output: 5
print(round(y, 2))  # Output: 3.14
print(max(z))     # Output: 5
print(min(z))     # Output: 1
print(sum(z))     # Output: 15
```
## Math Library 

Python's `math` library provides additional mathematical functions and constants. Some commonly used functions include: 

- `math.sqrt()`: Returns the square root of a number.
- `math.pow()`: Returns the value of a number raised to a power.
- `math.factorial()`: Returns the factorial of a number.
- `math.gcd()`: Returns the greatest common divisor of two numbers.
- `math.floor()`: Returns the largest integer less than or equal to a number.
- `math.trunc()`: Returns the integer part of a number, removing any fractional digits.

````python
import math     

x = 16
print(math.sqrt(x))        # Output: 4.0
print(math.pow(2, 3))      # Output: 8.0
print(math.factorial(5))   # Output: 120
print(math.gcd(12, 15))    # Output: 3
print(math.floor(3.7))     # Output: 3
print(math.trunc(3.7))     # Output: 3
````

## Random Library

Random numbers can be generated using Python's `random` library. Some commonly used functions include:

- `random.random()`: Returns a random float between 0.0 and 1.0.
- `random.randint(a, b)`: Returns a random integer between `a` and `b` (inclusive).
- `random.choice(seq)`: Returns a random element from a non-empty sequence.
- `random.shuffle(seq)`: Shuffles the elements of a list in place.  

```python
import random

print(random.random())          # Output: A random float between 0.0 and 1.0
print(random.randint(1, 10))    # Output: A random integer between 1 and 10 (inclusive)
print(random.choice(['apple', 'banana', 'cherry']))  # Output: A random element from the list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)  # Output: The list shuffled in random order
```

## Sets and Boleans

Sets and booleans are fundamental data types in Python that are often used in conjunction with numbers.

### Sets

A set is an unordered collection of unique elements. You can create a set using the `set()` function or by enclosing elements in curly braces `{}`.

#### Set Operations

* Definition (Unique elements only):
* Intersection (&):
* Union (|):
* Difference (-):

```python
# Creating sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}    

# Set operations
print(set_a & set_b)  # Intersection: {3, 4}
print(set_a | set_b)  # Union: {1, 2, 3, 4, 5, 6}
print(set_a - set_b)  # Difference: {1, 2}
```

### Boleans

A boolean value is either `True` or `False`. Booleans are often used in conditional statements and logical operations.

```python
x = True
y = False

print(x)  # Output: True
print(y)  # Output: False

# Boolean operations
print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False
```

## Key Learning and Interview Points

- Python supports multiple numeric types, including integers, floating-point numbers, and complex numbers.
- Python provides built-in functions for type conversion and arithmetic operations.
- Python supports different number bases and provides functions for base conversion.
- Floating-point precision can lead to rounding errors, while the `decimal` module allows for exact decimal arithmetic.
- Python's `math` and `random` libraries provide additional mathematical functions and random number generation capabilities.
- Sets are unordered collections of unique elements, and booleans represent truth values.
- Understanding these concepts is essential for solving problems and performing calculations in Python.
- In Python Integer size is infinite, it can grow as large as the memory allows, But default limit of covertingor print number in string is 4300 digits. If you try to convert a number larger than this limit to a string, it will raise a `ValueError`.


