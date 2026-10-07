squared_num = {x:x**2 for x in range(6)}
print(squared_num)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


keys = {"Masala", "Ginger", "Lemon"}
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
# Output: {'Ginger': 'Delicious', 'Lemon': 'Delicious', 'Masala': 'Delicious'}

new_dict = dict.fromkeys(keys, keys)
print(new_dict)
# Output: {'Ginger': {'Ginger', 'Lemon', 'Masala'}, 'Lemon': {'Ginger', 'Lemon', 'Masala'}, 'Masala': {'Ginger', 'Lemon', 'Masala'}}
