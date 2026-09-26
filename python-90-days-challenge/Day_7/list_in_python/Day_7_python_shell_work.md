# # Day 7: Raw Python Shell (REPL) Work

This log contains my raw terminal session while learning **Lists in Python**. From Day 1, I have made it a habit to practice different scenarios in the Python Shell for every new topic. This allows me to easily catch errors and understand the behind-the-scenes workings of Python.

I intentionally test unwanted and tricky edge cases to see exactly what happens and to understand how Python handles different errors. 

*Note: I didn't upload my shell logs for the first 6 days, but starting today (Day 7), I will be uploading my daily REPL work.*

```python-repl

keshav@ke-h-v:~/Python_The_Ultimate_World$ python3
Python 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> rom_cdrama = ["Hidden Love", "The First Frost", "Love is Sweet", "Only for Love"]
>>> print(rom_cdrama)
['Hidden Love', 'The First Frost', 'Love is Sweet', 'Only for Love']
>>> print(rom_cdrama[-1])
Only for Love
>>> rom_cdrama[-1] = "Timeless Love"
>>> print(rom_cdrama[-1])
Timeless Love
>>> print(rom_cdrama)
['Hidden Love', 'The First Frost', 'Love is Sweet', 'Timeless Love']
>>> rom_cdrama[1:2] = 
  File "<stdin>", line 1
    rom_cdrama[1:2] = 
                      ^
SyntaxError: invalid syntax
>>> rom_cdrama[1:2] = "Neverthless"
>>> print(rom_cdrama)
['Hidden Love', 'N', 'e', 'v', 'e', 'r', 't', 'h', 'l', 'e', 's', 's', 'Love is Sweet', 'Timeless Love']
>>> rom_cdrama = ["Hidden Love", "The First Frost", "Love is Sweet", "Only for Love"]
>>> rom_cdrama[1:2] = ["The Early Spring", "Timeless Love"]
>>> print(rom_cdrama)
['Hidden Love', 'The Early Spring', 'Timeless Love', 'Love is Sweet', 'Only for Love']
>>> rom_cdrama[1:3] = ["The First Frost"] 
>>> print(rom_cdrama)
['Hidden Love', 'The First Frost', 'Love is Sweet', 'Only for Love']
>>> rom_cdrama[1:3] = "The First Frost" 
>>> print(rom_cdrama)
['Hidden Love', 'T', 'h', 'e', ' ', 'F', 'i', 'r', 's', 't', ' ', 'F', 'r', 'o', 's', 't', 'Only for Love']
>>> rom_cdrama = ["Hidden Love", "The First Frost", "Love is Sweet", "Only for Love"]
>>> rom_cdrama[1:2:2] = "-------------" 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 13 to extended slice of size 1
>>> print(rom_cdrama)
['Hidden Love', 'The First Frost', 'Love is Sweet', 'Only for Love']
>>> rom_cdrama[1:2:2] = ["----------"] 
>>> print(rom_cdrama)
['Hidden Love', '----------', 'Love is Sweet', 'Only for Love']
>>> rom_cdrama = ["Hidden Love", "The First Frost", "Love is Sweet", "Only for Love"]
>>> rom_cdrama[2:2] = ["Timeless Love"]
>>> print(rom_cdrama)
['Hidden Love', 'The First Frost', 'Timeless Love', 'Love is Sweet', 'Only for Love']
>>> rom_cdrama[2:4] = []
>>> print(rom_cdrama)
['Hidden Love', 'The First Frost', 'Only for Love']
>>> rom_cdrama = ["Hidden Love", "The First Frost", "Love is Sweet", "Only for Love"]
>>> for cdrama in rom_cdrama:
...     print(cdrama)
... 
Hidden Love
The First Frost
Love is Sweet
Only for Love
>>> for cdrama in rom_cdrama:
...     print(cdrama, end"-")
  File "<stdin>", line 2
    print(cdrama, end"-")
                     ^^^
SyntaxError: invalid syntax
>>> for cdrama in rom_cdrama:
...     print(cdrama, end="-")
... 
Hidden Love-The First Frost-Love is Sweet-Only for Love->>> 
>>> if "Hidden Love" in rom_cdrama
  File "<stdin>", line 1
    if "Hidden Love" in rom_cdrama
                                  ^
SyntaxError: expected ':'
>>> if "Hidden Love" in rom_cdrama:
...     print("yes")
... 
yes
>>> rom_com.append("Vincenzo")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rom_com' is not defined
>>> rom_cdrama.append("Vincenzo")
>>> print(rom_cdrama)
['Hidden Love', 'The First Frost', 'Love is Sweet', 'Only for Love', 'Vincenzo']
>>> rom_cdrama.pop()
'Vincenzo'
>>> rom_cdrama.remove("Only for Love")
>>> print(rom_cdrama)
['Hidden Love', 'The First Frost', 'Love is Sweet']
>>> rom_cdrama.push("dhfjdsfjs")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'push'
>>> rom_cdrama.insert(1, "Only for Love")
>>> print(rom_cdrama)
['Hidden Love', 'Only for Love', 'The First Frost', 'Love is Sweet']
>>> rom_cdrama_copy = rom_cdrama.copy()
>>> rom_cdrama_copy is rom_cdrama
False
>>> rom_cdrama_copy == rom_cdrama
True
>>> rom_cdrama_copy.append(
... 
[1]+  Stopped                 python3
keshav@ke-h-v:~/Python_The_Ultimate_World$ python3
Python 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> rom_cdrama = ["Hidden Love", "The First Frost", "Love is Sweet", "Only for Love"]
>>> rom_cdrama_copy == rom_cdrama
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rom_cdrama_copy' is not defined
>>> print(rom_cdrama)
['Hidden Love', 'The First Frost', 'Love is Sweet', 'Only for Love']
>>> rom_cdrama_copy = rom_cdrama
>>> rom_cdrama_copy.append("Test")
>>> print(rom_cdrama)
['Hidden Love', 'The First Frost', 'Love is Sweet', 'Only for Love', 'Test']
>>> rom_cdrama_copy = rom_cdrama.copy()
>>> rom_cdrama.pop()
'Test'
>>> print(rom_cdrama)
['Hidden Love', 'The First Frost', 'Love is Sweet', 'Only for Love']
>>> print(rom_cdrama_copy)
['Hidden Love', 'The First Frost', 'Love is Sweet', 'Only for Love', 'Test']
>>> squared_num = [x**2 for x in range(10)]
>>> print(squared_num)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 

```