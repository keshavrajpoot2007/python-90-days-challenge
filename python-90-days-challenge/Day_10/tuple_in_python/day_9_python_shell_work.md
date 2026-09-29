# Day 10: Raw Python Shell (REPL) Work

This log contains my raw terminal session while learning **Tuples in Python**.



```python

keshav@ke-h-v:~/Python_The_Ultimate_World$ python3
Python 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> cartoon_names = (Motu Patlu, Shiva, Jungle Book, Pakdam Pakdai)
  File "<stdin>", line 1
    cartoon_names = (Motu Patlu, Shiva, Jungle Book, Pakdam Pakdai)
                     ^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> cartoon_names = ("Motu Patlu", "Shiva", "Jungle Book", "Pakdam Pakdai")
>>> print(cartoon_names)
('Motu Patlu', 'Shiva', 'Jungle Book', 'Pakdam Pakdai')
>>> cartoon_names[0]
'Motu Patlu'
>>> cartoon_names[-1]
'Pakdam Pakdai'
>>> cartoon_names[::-1
... ]
('Pakdam Pakdai', 'Jungle Book', 'Shiva', 'Motu Patlu')
>>> cartoon_names[0] = "Doora"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> len(cartoon_names)
4
>>> anime_name = ("Narutu", "AOT", "Doremon")
>>> anime_name
('Narutu', 'AOT', 'Doremon')
>>> all_cartoon_anime = cartoon_names + anime_name
>>> all
all(               all_cartoon_anime  
>>> all_cartoon_anime
('Motu Patlu', 'Shiva', 'Jungle Book', 'Pakdam Pakdai', 'Narutu', 'AOT', 'Doremon')
>>> all_cartoon_anime = ("Jungle Book", "Pakedam Pakdai", "Narutu", "AOT")
>>> all_cartoon_anime
('Jungle Book', 'Pakedam Pakdai', 'Narutu', 'AOT')
>>> anime_name, cartoon_names
(('Narutu', 'AOT', 'Doremon'), ('Motu Patlu', 'Shiva', 'Jungle Book', 'Pakdam Pakdai'))
>>> all_cartoon_anime = cartoon_names
>>> all_cartoon_anime id cartoon_names
  File "<stdin>", line 1
    all_cartoon_anime id cartoon_names
                      ^^
SyntaxError: invalid syntax
>>> all_cartoon_anime is cartoon_names
True
>>> all_cartoon_anime = ('Narutu', 'AOT', 'Doremon')
>>> all_cartoon_anime = cartoon_names
>>> all_cartoon_anime = ('Motu Patlu', 'Shiva', 'Jungle Book', 'Pakdam Pakdai')
>>> all_cartoon_anime is cartoon_names
False
>>> 
>>> all_cartoon_anime = cartoon_names.copy()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'copy'
>>> all_cartoon_anime = ('Motu Patlu', 'Shiva', 'Jungle Book', 'Pakdam Pakdai', 'Pakdam Pakdai')
>>> "Shiva" in all_cartoon_anime
True
>>> all_cartoon_anime.count("Pakdam Pakdai")
2
>>> all_cartoon_anime.count("AOT")
0
>>> cartoon_names
('Motu Patlu', 'Shiva', 'Jungle Book', 'Pakdam Pakdai')
>>> ('
  File "<stdin>", line 1
    ('
     ^
SyntaxError: unterminated string literal (detected at line 1)
>>> ('motu patlu', 'shiva', 'jungle book', 'pakdam pakdai') = cartoon_names
  File "<stdin>", line 1
    ('motu patlu', 'shiva', 'jungle book', 'pakdam pakdai') = cartoon_names
     ^^^^^^^^^^^^
SyntaxError: cannot assign to literal
>>> (motu patlu, shiva, jungle book, pakdam pakdai) = cartoon_names
  File "<stdin>", line 1
    (motu patlu, shiva, jungle book, pakdam pakdai) = cartoon_names
     ^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> (motu_patlu, shiva, jungle_book, pakdam_pakdai) = cartoon_names
>>> motu_patlu
'Motu Patlu'
>>> type(cartoon_names)
<class 'tuple'>
>>> all_animation = ("cartton", ("Doora", "Motu Patlu"), "anime", ("AOT", "Naruto"))
>>> all_
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'all_' is not defined. Did you mean: 'all'?
>>> all_animation
('cartton', ('Doora', 'Motu Patlu'), 'anime', ('AOT', 'Naruto'))
>>> 

```