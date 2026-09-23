print(type(True))
print(type(False))
# Output: <class 'bool'>, because True and False are of boolean type in Python.

print(True == 1) # Output: True, because True is equivalent to 1 in Python.
print(False == 0) # Output: True, because False is equivalent to 0 in Python.

print(True is 1) # Output: False, because True is not the same object as 1.
print(False is 0) # Output: False, because False is not the same object as 0.


print(int(True)) # Output: 1, because True is equivalent to 1 in Python.
print(int(False)) # Output: 0, because False is equivalent to 0 in Python

print(bool(10)) # Output: True, because any non-zero integer is considered True in Python.
print(bool(0)) # Output: False, because 0 is considered False in Python.

print(bool(-5)) # Output: True, because any non-zero integer is considered True in Python.
print(bool(0.0)) # Output: False, because 0.0 is considered False in Python.

print(bool(0.1)) # Output: True, because 0.1 is non-zero integer.


# Operations with boolean values

print(True and False) # Output: False, because both operands need to be True for the result to be True.
print(True or False) # Output: True, because at least one operand is True.
print(not True) # Output: False, because not operator negates the boolean value.

print(True and True) # Output: True, because both operands are True.
print(False or False) # Output: False, because both operands are False.

print(True + True) # Output: 2, because True is equivalent to 1 in Python.
print(True + False) # Output: 1, because True is equivalent to 1 and False is equivalent to 0 in Python.
print(False + False) # Output: 0, because both operands are equivalent to 0 in Python.

print(True * 5) # Output: 5, because True is equivalent to 1 in Python.
print(False * 3) # Output: 0, because False is equivalent to 0 in Python.

print(True > False) # Output: True, because True is equivalent to 1 and False is equivalent to 0 in Python.
print(False < True) # Output: True, because False is equivalent to 0 and True

print(oct(True)) # Output: 0o1, because True is equivalent to 1 in Python.
print(hex(False)) # Output: 0x0, because False is equivalent to 0 in Python.

