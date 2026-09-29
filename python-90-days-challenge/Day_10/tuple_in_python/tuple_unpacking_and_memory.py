cartoon_names = ("Motu Patlu", "Shiva", "Jungle Book", "Pakdam Pakdai")

# 1. Tuple Unpacking
# Assigning tuple values to individual variables in one line
(motu_patlu, shiva, jungle_book, pakdam_pakdai) = cartoon_names

print("Unpacked Variable 1:", motu_patlu) # Output: Motu Patlu
print("Unpacked Variable 2:", jungle_book) # Output: Jungle Book

# 2. Memory and Copying
# Since tuples are immutable, Python doesn't provide a .copy() method.
try:
    new_tuple = cartoon_names.copy()
    
except AttributeError as e:
    print("\nCopy Test Passed! Error:", e)
    
# Assigning a tuple to a new variable just creates a reference.
# But if you create a new tuple with the exact same values, it creates a new object in memory.
identical_tuple = ('Motu Patlu', 'Shiva', 'Jungle Book', 'Pakdam Pakdai')
print("\nIs it the exact same object in memory?", identical_tuple is cartoon_names) # Output: False

