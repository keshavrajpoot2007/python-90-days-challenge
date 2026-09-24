# Searching, Counting, and Length
# .find() - finds the first occurrence of a substring, returns -1 if not found
# .count() - counts how many times a substring appears in the string
# len() - returns the total number of characters in the string
# in - checks if a substring exists in the string (returns True or False)


Movie_Quote = "May the Force be with you, always with you."


# Find

Find_Force = Movie_Quote.find("Force") # Returns the starting index of "Force"
Find_Jedi = Movie_Quote.find("Jedi") # Returns -1 because "Jedi" is not in the string

print("Searching in Strings:")
print("Find_Force:", Find_Force) # Output: 8
print("Find_Jedi:", Find_Jedi) # Output: -1
print("\n")


# Count

Count_With = Movie_Quote.count("with") # Counts total occurrences of the word "with"
Count_Space = Movie_Quote.count(" ") # Counts total spaces in the string

print("Counting in Strings:")
print("Count_With:", Count_With) # Output: 2
print("Count_Space:", Count_Space) # Output: 8
print("\n")


# Length

Total_Length = len(Movie_Quote) # Counts total characters including spaces and punctuation

print("Length of String:")
print("Total_Length:", Total_Length) # Output: 43
print("\n")


# Membership Operator (in)

Has_Force = "Force" in Movie_Quote # Checks if "Force" exists in the quote
Has_Dark_Side = "Dark Side" in Movie_Quote # Checks if "Dark Side" exists in the quote

print("Membership Operator (in):")
print("Has_Force:", Has_Force) # Output: True
print("Has_Dark_Side:", Has_Dark_Side) # Output: False
print("\n")