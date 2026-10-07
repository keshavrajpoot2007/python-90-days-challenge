rom_cdrama = ["Hidden Love", "The First Frost", "Love is Sweet", "Only for Love"]

# Iterating over a list
print("Iterating with new line:")
for cdrama in rom_cdrama:
    print(cdrama)

print("\nIterating in one line with custom end:")
for cdrama in rom_cdrama:
    print(cdrama, end="-")
print("\n")

# Membership check
if "Hidden Love" in rom_cdrama:
    print("Yes, 'Hidden Love' is in the list!")

# List Methods
rom_cdrama.append("The Early Spring")  # Adds at the end
print("After append:", rom_cdrama)

rom_cdrama.pop()  # Removes and returns the last element
print("After pop:", rom_cdrama)

rom_cdrama.remove("Only for Love")  # Removes the first occurrence of the specific value
print("After remove:", rom_cdrama)

rom_cdrama.insert(1, "Only for Love")  # Inserts value at specific index
print("After insert:", rom_cdrama)