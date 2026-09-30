top_cdramas = ("Hidden Love", "The First Frost", "Love is Sweet")
print("\n", top_cdramas)

# tuple is immutable
try:
    top_cdramas[1] = "Timeless Love"
except TypeError as e:
    print("\nImutability test Pass!, Error: ", e)
    
# tupple unpacking
[rank1, rank2, rank3] = top_cdramas

print("\n", rank1, rank2, rank3)