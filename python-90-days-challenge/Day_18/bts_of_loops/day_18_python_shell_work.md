# Day 9: Raw Python Shell (REPL) Work

This log contains my raw terminal session while learning **Behind the scene of Loops in Python**.


```python

keshav@ke-h-v:~/Python_The_Ultimate_World/python-90-days-challenge/Day_18/bts_of_loops$ python3
Python 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
>>> open('example.txt')
<_io.TextIOWrapper name='example.txt' mode='r' encoding='UTF-8'>
>>> f = open('example.txt')
>>> f.readline()
'line 1\n'
>>> f.readline()
'line 2\n'
>>> f.readline()
'line 3\n'
>>> f.readline()
'line 4'
>>> f.readline()
''
>>> f.readline()
''
>>> f = open('example.txt')
>>> f.__next__()
'line 1\n'
>>> f.__next__()
'line 2\n'
>>> f.__next__()
'line 3\n'
>>> f.__next__()
'line 4'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> for line in open('chai'):
...     print(line)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'chai'
>>> for line in open('example.txt'):
...     print(line)
... 
line 1

line 2

line 3

line 4
>>> for line in open('example.txt'):
...     print(line,end = "")
... 
line 1
line 2
line 3
line 4>>> 
>>> 
>>> f = open('example.txt')
>>> while True
  File "<stdin>", line 1
    while True
              ^
SyntaxError: expected ':'
>>> while True:
...     line = f.readline()
...     if not line:
...             break
...     print(line)
... 
line 1

line 2

line 3

line 4
>>> 
>>> test = "Keshav"
>>> if not test:
...     print("abcd")
... 
>>> test = ""
>>> if not test:
...     print("abcd")
... 
abcd
>>> myList = [1,2,3,4]
>>> I = iter(myList)
>>> i
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'i' is not defined. Did you mean: 'I'?
>>> I
<list_iterator object at 0x7f0619f1f970>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x7f0619f1f970>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I
<list_iterator object at 0x7f0619f1f970>
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> f = open('example.txt')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
>>> myNewList = [1,2,3]
>>> iter(myNewLisr) is myNewList
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myNewLisr' is not defined. Did you mean: 'myNewList'?
>>> iter(myNewList) is myNewList
False
>>> D = {'a':1,'b':2}
>>> for key in D.keys():
...     print(key)
... 
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x7f061a8b2200>
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'i' is not defined. Did you mean: 'I'?
>>> I.__next__()
'a'
>>> next(I)
'b'
>>> range(5)
range(0, 5)
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 

```