# Day 9: Raw Python Shell (REPL) Work

This log contains my raw terminal session while learning **Dictionaries in Python**.


```python

keshav@ke-h-v:~/Python_The_Ultimate_World$ python3
Python 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> tea_shop = {
... "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
... "Tea": {"Green": "Mild", "Black": "Strong"}
... }
>>> print(tea shop)
  File "<stdin>", line 1
    print(tea shop)
          ^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(tea_shop)
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]
'Zesty'
>>> tea_shop["chai["Ginger"]"]
  File "<stdin>", line 1
    tea_shop["chai["Ginger"]"]
             ^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> tea_shop["chai"]["Ginger"]
'Zesty'
>>> squared_num = {x:x**2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}
>>> keys = {"Masala", "Ginger", "Lemon"}
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys, default_value)
>>> new_dict
{'Ginger': 'Delicious', 'Lemon': 'Delicious', 'Masala': 'Delicious'}
>>> new_dict = dict.fromkeys(keys, keys)
>>> new_dict
{'Ginger': {'Ginger', 'Lemon', 'Masala'}, 'Lemon': {'Ginger', 'Lemon', 'Masala'}, 'Masala': {'Ginger', 'Lemon', 'Masala'}}
>>> 

```