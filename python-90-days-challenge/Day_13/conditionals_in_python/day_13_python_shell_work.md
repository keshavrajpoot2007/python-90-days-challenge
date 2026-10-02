# Day 12: Raw Python Shell (REPL) Work

This log contains my raw terminal session while learning **Conditionals in Python**.


```python

keshav@ke-h-v:~/Python_The_Ultimate_World$ python3
Python 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
>>> a = 20
>>> if a < 15:
...     print("a < 15")
... elif a <= 20:
...     print("a <= 20")
... else:
...     print("a > 20")
... 
a <= 20
>>> b = 30
>>> elif b < 30:
  File "<stdin>", line 1
    elif b < 30:
    ^^^^
SyntaxError: invalid syntax
>>> c = 20
>>> if c < 20:
...     print("c < 20")
... elif c = 20:
  File "<stdin>", line 3
    elif c = 20:
         ^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> c = 20
>>> if c < 20:
...     print("c < 20")
... elif c == 20:
...   print("c == 20")
... else:
...             print("c >20")
... 
c == 20
>>> import random
>>> random.choice('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Random.choice() takes 2 positional arguments but 8 were given
>>> random.choices('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Random.choices() takes from 2 to 3 positional arguments but 8 were given
>>> random.choices(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
['Tuesday']
>>> score = 40
>>> grade = 'A' if score >=90: 'b' elif score >= 80:
  File "<stdin>", line 1
    grade = 'A' if score >=90: 'b' elif score >= 80:
                             ^
SyntaxError: invalid syntax
>>> grade = 'A' if score >=90 'b' elif score >= 80
  File "<stdin>", line 1
    grade = 'A' if score >=90 'b' elif score >= 80
            ^^^^^^^^^^^^^^^^^
SyntaxError: expected 'else' after 'if' expression
>>> if c = 20:
  File "<stdin>", line 1
    if c = 20:
       ^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> if c == 20:
...     print(c)
... elif c < 20
  File "<stdin>", line 3
    elif c < 20
               ^
SyntaxError: expected ':'
>>> if c == 20:
...     print(c)
... exit()
  File "<stdin>", line 3
    exit()
    ^^^^
SyntaxError: invalid syntax
>>> exit()
keshav@ke-h-v:~/Python_The_Ultimate_World$ Python3
Command 'Python3' not found, did you mean:
  command 'cython3' from deb cython3 (3.0.7-2ubuntu1)
  command 'cython3' from deb cython3-legacy (0.29.36-3ubuntu1)
  command 'python3' from deb python3 (3.12.3-0ubuntu2.1)
Try: sudo apt install <deb name>
keshav@ke-h-v:~/Python_The_Ultimate_World$ python3
Python 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
>>> weather = sunny
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sunny' is not defined
>>> weather = "sunny"
>>> if weather is "sunny":
...     print(sunny)
... 
<stdin>:1: SyntaxWarning: "is" with 'str' literal. Did you mean "=="?
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'sunny' is not defined
>>> distance = 3.09
>>> if distance >3
  File "<stdin>", line 1
    if distance >3
                  ^
SyntaxError: expected ':'
>>> if distance >3:
...     print("working")
... 
working
>>> 

```