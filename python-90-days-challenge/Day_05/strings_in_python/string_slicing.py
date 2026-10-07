# String Slicing
# Format:-
#        string[index] - for access one element
#        string[start:end] - for access multiple elements
#        string[start:end:step] - for access multiple elements with step

# index - Position of an element in a string
# start - Starting index of the slice
# end - Ending index of the slice (not included in the slice, in other words, end is exclusive)
# step - Step size for the slice



Num_List = "0123456789"

print(Num_List) # Output: 0123456789


# Indexing: string[index] - for access one element

Element_1 = Num_List[0]
Element_2 = Num_List[1]
Last_Element = Num_List[-1]
Second_Last_Element = Num_List[-2]

print("\n")
print("Indexing: string[index] - for access one element")
print("Element_1:", Element_1) # Output: 0
print("Element_2:", Element_2) # Output: 1
print("Last_Element:", Last_Element) # Output: 9
print("Second_Last_Element:", Second_Last_Element) # Output: 8
print("\n")


# Slicing: string[start:end] - for access multiple elements

Slice_1 = Num_List[0:5] # Access all element from index 0 to 4
Slice_2 = Num_List[5:10] # Access all element from index 5 to 9
Slice_3 = Num_List[:] # Access all elements
Slice_4 = Num_List[2:] # Access all elements from index 2 to end
Slice_5 = Num_List[:5] # Access all elements from start to index 4 

# Negative Index Slicing: string[start:end] - for access multiple elements using negative index

Negative_Slice_1 = Num_List[:-1] # Access all elements except the last one
Negative_Slice_3 = Num_List[-5:] # Access all elements from index -5 to end
Negative_Slice_2 = Num_List[-5:-1] # Access all elements from index -5 to -2
Negative_Slice_4 = Num_List[-5:-3] # Access all elements from index -5 to -4


print("Slicing: string[start:end] - for access multiple elements")
print("Slice_1:", Slice_1) # Output: 01234
print("Slice_2:", Slice_2) # Output: 56789
print("Slice_3:", Slice_3) # Output: 0123456789
print("Slice_4:", Slice_4) # Output: 23456789
print("Slice_5:", Slice_5) # Output: 01234
print("\n")
print("By Negative Index")
print("Negative_Slice_1:", Negative_Slice_1) # Output: 012345678
print("Negative_Slice_2:", Negative_Slice_2) # Output: 5678
print("Negative_Slice_3:", Negative_Slice_3) # Output: 56789
print("Negative_Slice_4:", Negative_Slice_4) # Output: 56
print("\n")


# Extended Slicing: string[start:end:step] - for access multiple elements with step

Extended_Slice_1 = Num_List[0:10:2] # Access all elements from index 0 to 9 with step 2
Extended_Slice_2 = Num_List[::2] # Access all elements with step 2
Extended_Slice_3 = Num_List[1:10:2] # Access all elements from index 1 to 9 with step 2
Exrended_Slice_4 = Num_List[1::3] # Access all elements from index 1 to end with step 2
Extended_Slice_5 = Num_List[3:9:3] # Access all elements from index 3 to 8 with step 3

# For geting the reverse of a string we can use negative step
Reverse_Slice_1 = Num_List[::-1] # Access all elements in reverse order
Reverse_Slice_2 = Num_List[9:0:-1] # Access all elements from index 9 to 1 in reverse order
Reverse_Slice_3 = Num_List[9::-2] # Access all elements from index 9 to 0 in reverse order
Reverse_Slice_4 = Num_List[-3:-8:-1] # Access all elements from index -3 to -7 in reverse order
Reverse_Slice_5 = Num_List[-1:1:-1] # Access all elements from index -1 to 2 in reverse order

print("Extended Slicing: string[start:end:step] - for access multiple elements with step")
print("Extended_Slice_1:", Extended_Slice_1) # Output: 02468
print("Extended_Slice_2:", Extended_Slice_2) # Output: 02468
print("Extended_Slice_3:", Extended_Slice_3) # Output: 13579
print("Exrended_Slice_4:", Exrended_Slice_4) # Output: 147
print("Extended_Slice_5:", Extended_Slice_5) # Output: 36
print("\n")
print("Reverse Slicing: string[::-1] - for access multiple elements in reverse order")
print("Reverse_Slice_1:", Reverse_Slice_1) # Output: 9876543210
print("Reverse_Slice_2:", Reverse_Slice_2) # Output: 987654321
print("Reverse_Slice_3:", Reverse_Slice_3) # Output: 97531
print("Reverse_Slice_4:", Reverse_Slice_4) # Output: 76543
print("Reverse_Slice_5:", Reverse_Slice_5) # Output: 98765432
print("\n")





