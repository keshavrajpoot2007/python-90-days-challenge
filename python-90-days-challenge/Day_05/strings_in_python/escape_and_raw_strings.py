# Escape Sequences & Raw Strings
# \n - creates a new line
# \" - escapes double quotes so they can be printed inside a string
# \\ - escapes a backslash
# r"" - raw string, ignores escape characters and prints string exactly as written


# New Line

Multi_Line_Text = "First Rule of Fight Club:\nYou do not talk about Fight Club."
            
print("Escape Sequence: New Line (\\n)")
print(Multi_Line_Text) 
# Output: 
# First Rule of Fight Club:
# You do not talk about Fight Club.
print("\n")


# Escaping Quotes

Famous_Quote = "He said, \"I am Iron Man.\""

print("Escape Sequence: Double Quotes (\\\")")
print("Famous_Quote:", Famous_Quote) # Output: He said, "I am Iron Man."
print("\n")


# Escaping Backslash (useful for file paths)

Normal_Path = "C:\\Users\\Keshav\\Downloads" # Using double backslash to print a single backslash

print("Escape Sequence: Backslash (\\\\)")
print("Normal_Path:", Normal_Path) # Output: C:\Users\Keshav\Downloads
print("\n")


# Raw Strings (r"")
# Useful when we don't want to double every backslash, especially in Windows file paths

Raw_Path = r"C:\Users\Keshav\Downloads" 
Raw_Quote_Path = r"C:\Users\Keshav\NewFolder\n_file.txt" # Here \n is treated as normal text, not a new line

print("Raw Strings (r\"\"):")
print("Raw_Path:", Raw_Path) # Output: C:\Users\Keshav\Downloads
print("Raw_Quote_Path:", Raw_Quote_Path) # Output: C:\Users\Keshav\NewFolder\n_file.txt
print("\n")