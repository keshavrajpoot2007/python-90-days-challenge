# Creating a Tuple
cartoon_names = ("Motu Patlu", "Shiva", "Jungle Book", "Pakdam Pakdai")
print("Original Tuple:", cartoon_names)

# 1. Indexing and Slicing (Same as Lists)
print("First Cartoon:", cartoon_names[0])
print("Last Cartoon:", cartoon_names[-1])
print("Reversed Tuple:", cartoon_names[::-1])

# 2. The Core Difference: IMMUTABILITY
# Tuples cannot be changed once created. 
try:
    cartoon_names[0] = "Dora"
except TypeError as e:
    print("\nImmutability Test Passed! Error:", e)
    # Output: 'tuple' object does not support item assignment