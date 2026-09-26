rom_cdrama = ["Hidden Love", "The First Frost", "Love is Sweet", "Only for Love"]

# The Trap of Direct Assignment (Reference)
rom_cdrama_ref = rom_cdrama 
rom_cdrama_ref.append("Test") 
# Both lists change because they point to the exact same memory location!
print("Original List changed due to reference:", rom_cdrama)


# The Solution: .copy() method
rom_cdrama.pop() # Removing the 'Test' added above
rom_cdrama_copy = rom_cdrama.copy() # Creates a new object in memory

print("\nIs it the same memory object? :", rom_cdrama_copy is rom_cdrama) # False
print("Are the values identical? :", rom_cdrama_copy == rom_cdrama) # True

rom_cdrama_copy.append("New Drama")
print("Original List (Unchanged):", rom_cdrama)
print("Copied List (Changed):", rom_cdrama_copy)


# List Comprehension: A shorter way to create lists using a for-loop inside brackets
squared_num = [x**2 for x in range(10)]
print("\nSquared Numbers:", squared_num)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]