# ==========================================
# Challenge 2: The Ultimate Matchmaker (zip)
# ==========================================
# Problem: You have two lists: one containing characters and another containing 
# their respective shows. Use the zip() function to iterate over both lists 
# simultaneously and print their relationship.

# characters = ["Sang Zhi", "Duan Jiaxu", "Tony Stark", "Peter Parker"]
# shows = ["Hidden Love", "Hidden Love", "Iron Man", "Spider-Man"]

# '''
# Expected Output:
# Sang Zhi is from Hidden Love
# Duan Jiaxu is from Hidden Love
# Tony Stark is from Iron Man
# Peter Parker is from Spider-Man
# '''

# Write your code below:

characters = ["Sang Zhi", "Duan Jiaxu", "Tony Stark", "Peter Parker"]
shows = ["Hidden Love", "Hidden Love", "Iron Man", "Spider-Man"]

for c, s in zip(characters, shows):
    print(f"{c} is from {s}")