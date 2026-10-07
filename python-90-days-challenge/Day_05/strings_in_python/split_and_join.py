# Spliting and Joining Strings
# .split() - splits a string into a list of substrings based on a delimiter
# .join() - joins a list of strings into a single string with a specified delimiter

Anime_List_String = "Attack on Titan, Death Note, Vinland Saga, Mushoko Tensei, Doremon"

# Splitting the string into a list of substrings

Split_By_Comma = Anime_List_String.split(",") # Split_By_Comma will be a list of strings, where each string is a substring of Anime_List_String that was separated by a comma.

Split_By_Space = Anime_List_String.split(" ") # Split_By_Space will be a list of strings, where each string is a substring of Anime_List_String that was separated by a space.

Split_By_Comma_Space = Anime_List_String.split(", ") # Split_By_Comma_Space will be a list of strings, where each string is a substring of Anime_List_String that was separated by a comma and space.

Split_By_Default = Anime_List_String.split() # .split() by default use space for seperation.


# Printing Split Results

print("Splitting Strings:")
print("Original_String:", Anime_List_String)
print("\n")

print("Split_By_Comma:", Split_By_Comma) 
# Output: ['Attack on Titan', ' Death Note', ' Vinland Saga', ' Mushoko Tensei', ' Doremon']  <- (Notice the extra spaces at the start of words)

print("Split_By_Space:", Split_By_Space) 
# Output: ['Attack', 'on', 'Titan,', 'Death', 'Note,', 'Vinland', 'Saga,', 'Mushoko', 'Tensei,', 'Doremon']

print("Split_By_Comma_Space:", Split_By_Comma_Space) 
# Output: ['Attack on Titan', 'Death Note', 'Vinland Saga', 'Mushoko Tensei', 'Doremon'] <- (Cleanest split)

print("Split_By_Default:", Split_By_Default) 
# Output: ['Attack', 'on', 'Titan,', 'Death', 'Note,', 'Vinland', 'Saga,', 'Mushoko', 'Tensei,', 'Doremon']
print("\n")


# ------------------------------------------------------------------------------------------------------


# Joining Strings: .join() - joins a list of strings into a single string using a separator

Characters_List = ["Eren", "Light", "Thorfinn", "Rudeus", "Nobita"]

Join_With_Comma_Space = ", ".join(Characters_List) # Joins list elements with a comma and a space
Join_With_Dash = "-".join(Characters_List) # Joins list elements with a dash
Join_With_Underscore = "_".join(Characters_List) # Joins list elements with an underscore
Join_With_Space = " ".join(Characters_List) # Joins list elements with a single space
Join_Without_Space = "".join(Characters_List) # Joins list elements without any space or separator

# Printing Join Results

print("Joining Strings:")
print("Original_List:", Characters_List)
print("\n")

print("Join_With_Comma_Space:", Join_With_Comma_Space) 
# Output: Eren, Light, Thorfinn, Rudeus, Nobita

print("Join_With_Dash:", Join_With_Dash) 
# Output: Eren-Light-Thorfinn-Rudeus-Nobita

print("Join_With_Underscore:", Join_With_Underscore) 
# Output: Eren_Light_Thorfinn_Rudeus_Nobita

print("Join_With_Space:", Join_With_Space) 
# Output: Eren Light Thorfinn Rudeus Nobita

print("Join_Without_Space:", Join_Without_Space) 
# Output: ErenLightThorfinnRudeusNobita
print("\n")