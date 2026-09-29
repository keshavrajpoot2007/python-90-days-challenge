cartoon_names = ("Motu Patlu", "Shiva", "Jungle Book", "Pakdam Pakdai")
anime_names = ("Naruto", "AOT", "Doraemon")

# 1. Concatenation (Adding two tuples creates a brand NEW tuple)
all_animations = cartoon_names + anime_names
print("Concatenated Tuple:", all_animations)

# 2. Built-in Methods (Tuples only have 2 methods: count and index)
duplicates_tuple = ('Motu Patlu', 'Shiva', 'Pakdam Pakdai', 'Pakdam Pakdai')
print("\nCount of 'Pakdam Pakdai':", duplicates_tuple.count("Pakdam Pakdai")) # Output: 2
print("Count of 'AOT':", duplicates_tuple.count("AOT")) # Output: 0

# 3. Nested Tuples
all_categories = ("Cartoons", ("Dora", "Motu Patlu"), "Anime", ("AOT", "Naruto"))
print("\nNested Tuple Access:", all_categories[1][1]) # Output: Motu Patlu