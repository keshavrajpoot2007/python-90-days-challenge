# Day 8: Raw Python Shell (REPL) Work

This log contains my raw terminal session while learning **Dictionaries in Python**.


```python

keshav@ke-h-v:~/Python_The_Ultimate_World$ python3
Python 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> songs_artist = {"Blinding Lights": "The Weeknd", "Mockingbird": "Eminem", "Tere liye": "Atif Aslam", "Darkside": "Neoni", "Fairytale": "Alexender Rybak"}
>>> so
songs_artist  sorted(       
>>> songs_artist
{'Blinding Lights': 'The Weeknd', 'Mockingbird': 'Eminem', 'Tere liye': 'Atif Aslam', 'Darkside': 'Neoni', 'Fairytale': 'Alexender Rybak'}
>>> songs_artist["Blinding Lights"]
'The Weeknd'
>>> songs_artist["Blinding Lights", "Dardside"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: ('Blinding Lights', 'Dardside')
>>> songs_artist["Blinding Lights": "Dardside"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: slice('Blinding Lights', 'Dardside', None)
>>> songs_artist["Blinding Lights", "Darkside"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: ('Blinding Lights', 'Darkside')
>>> songs_artist.get("Mockingbird")
'Eminem'
>>> songs_artist.get("Mockingbirds")
>>> songs_artist.get("Mockingbirdss")
>>> songs_artist.get("Darksides")
>>> songs_artist.get("Bilnding Lights")
>>> songs_artist.get("Bilnding Lightt")
>>> songs_artist
{'Blinding Lights': 'The Weeknd', 'Mockingbird': 'Eminem', 'Tere liye': 'Atif Aslam', 'Darkside': 'Neoni', 'Fairytale': 'Alexender Rybak'}
>>> songs_artist["Tere Liye"] = "Shreya Ghosal"
>>> songs_artist
{'Blinding Lights': 'The Weeknd', 'Mockingbird': 'Eminem', 'Tere liye': 'Atif Aslam', 'Darkside': 'Neoni', 'Fairytale': 'Alexender Rybak', 'Tere Liye': 'Shreya Ghosal'}
>>> songs_artist.remove("Tere Liye")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'remove'
>>> songs_artist["Tere Liye"] = ""
>>> songs_artist
{'Blinding Lights': 'The Weeknd', 'Mockingbird': 'Eminem', 'Tere liye': 'Atif Aslam', 'Darkside': 'Neoni', 'Fairytale': 'Alexender Rybak', 'Tere Liye': ''}
>>> songs_artist.pop("Tere Liye")
''
>>> songs_artist
{'Blinding Lights': 'The Weeknd', 'Mockingbird': 'Eminem', 'Tere liye': 'Atif Aslam', 'Darkside': 'Neoni', 'Fairytale': 'Alexender Rybak'}
>>> songs_artist["Tere liye"] = 
  File "<stdin>", line 1
    songs_artist["Tere liye"] = 
                                ^
SyntaxError: invalid syntax
>>> songs_artist["Tere liye"] = "Shreya Ghosal"
>>> songs_artist
{'Blinding Lights': 'The Weeknd', 'Mockingbird': 'Eminem', 'Tere liye': 'Shreya Ghosal', 'Darkside': 'Neoni', 'Fairytale': 'Alexender Rybak'}
>>> 
>>> for song in songs_artist
  File "<stdin>", line 1
    for song in songs_artist
                            ^
SyntaxError: expected ':'
>>> for song in songs_artist:
...     print(song)
... 
Blinding Lights
Mockingbird
Tere liye
Darkside
Fairytale
>>> for song in songs_artist:
...     print(song, " - ", songs_artist[song])
... 
Blinding Lights  -  The Weeknd
Mockingbird  -  Eminem
Tere liye  -  Shreya Ghosal
Darkside  -  Neoni
Fairytale  -  Alexender Rybak
>>> song
song          songs_artist  
>>> song
song          songs_artist  
>>> songs_artist.items()
dict_items([('Blinding Lights', 'The Weeknd'), ('Mockingbird', 'Eminem'), ('Tere liye', 'Shreya Ghosal'), ('Darkside', 'Neoni'), ('Fairytale', 'Alexender Rybak')])
>>> for key, value in songs_artist.items():
...     print(key, value)
... 
Blinding Lights The Weeknd
Mockingbird Eminem
Tere liye Shreya Ghosal
Darkside Neoni
Fairytale Alexender Rybak
>>> for key in songs_artist.items():
...     print(key)
... 
('Blinding Lights', 'The Weeknd')
('Mockingbird', 'Eminem')
('Tere liye', 'Shreya Ghosal')
('Darkside', 'Neoni')
('Fairytale', 'Alexender Rybak')
>>> for key, value in songs_artist.items():
...     print(value)
... 
The Weeknd
Eminem
Shreya Ghosal
Neoni
Alexender Rybak
>>> for key, value, test in songs_artist.items():
...     print(key)
...     print(value)
...     print(test)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 3, got 2)
>>> for key, value, test, test2 in songs_artist.items():
...     print(test)
...     print(test2)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 4, got 2)
>>> if Eminem in songs_artist
  File "<stdin>", line 1
    if Eminem in songs_artist
                             ^
SyntaxError: expected ':'
>>> if Eminem in songs_artist:
...     print("Yes")
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Eminem' is not defined
>>> if "Eminem" in songs_artist:
...     print("Yes")
... 
>>> if Darkside in songs_artist:
...     print("Yes")
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Darkside' is not defined
>>> if "Darkside" in songs_artist:
...     print("Yes")
... 
Yes
>>> if "Darkside" in songs_artist.items():
...     print("Yes")
... 
>>> if "Eminem" in songs_artist.items():
...     print("Yes")
... 
>>> if "Eminem" in songs_artist.items[]:
  File "<stdin>", line 1
    if "Eminem" in songs_artist.items[]:
                                      ^
SyntaxError: invalid syntax
>>> if "Eminem" in songs_artist.items[Mockingbird]:
...     print("Yes")
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Mockingbird' is not defined
>>> if "Eminem" in songs_artist[Mockingbird]:
...     print("Yes")
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Mockingbird' is not defined
>>> if "Eminem" in songs_artist["Mockingbird"]:
...     print("Yes")
... 
Yes
>>> print(len(songs_artist)
... )
5
>>> print(songs_artist)
{'Blinding Lights': 'The Weeknd', 'Mockingbird': 'Eminem', 'Tere liye': 'Shreya Ghosal', 'Darkside': 'Neoni', 'Fairytale': 'Alexender Rybak'}
>>> songs_artist["Rap God"] = "Eminem"
>>> songs_artist
{'Blinding Lights': 'The Weeknd', 'Mockingbird': 'Eminem', 'Tere liye': 'Shreya Ghosal', 'Darkside': 'Neoni', 'Fairytale': 'Alexender Rybak', 'Rap God': 'Eminem'}
>>> songs_artist["Mockingbird"] == songs_artist["Rap God"]
True
>>> songs_artist["Mockingbird"] is songs_artist["Rap God"]
True
>>> dict()
{}
>>> songs_artist.pop("Rap God")
'Eminem'
>>> songs_artist
{'Blinding Lights': 'The Weeknd', 'Mockingbird': 'Eminem', 'Tere liye': 'Shreya Ghosal', 'Darkside': 'Neoni', 'Fairytale': 'Alexender Rybak'}
>>> songs_artist.popitem()
('Fairytale', 'Alexender Rybak')
>>> del songs_artist["Tere Liye")
  File "<stdin>", line 1
    del songs_artist["Tere Liye")
                                ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> del songs_artist["Tere Liye"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Tere Liye'
>>> del songs_artist["Tere liye"]
>>> songs_artist
{'Blinding Lights': 'The Weeknd', 'Mockingbird': 'Eminem', 'Darkside': 'Neoni'}
>>> 

```