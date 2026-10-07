sports_players = {"Cricket": "Virat Kholi", "Football": "Cristiano Ronaldo", "Racing": "Usain Bolt"}
print(sports_players)

# # <------------------------------- Access elements using loops ------------------------------->

# Access keys using loop
print("\nKeys:-")
for key in sports_players:
    print(key)
    
# Access values using loop
print("\nValues:-")
for value in sports_players:
    print(sports_players[value])
    
# Acces elements using items()

print("\nKeys and Values:-")
for key, value in sports_players.items():
    print(key, " - ", value)
    
    

# <------------------------------- Check elements using conditions ------------------------------->

# Check key in dict
if "Cricket" in sports_players:
    print("Cricket is present in sports_player")

else:
    print("Cricket is not present in sports_player")
    
    
# Check values in key
if "Usain Bolt" in sports_players["Racing"]:
    print("Usain Bolt is a Racing Athlete.")

else:
    print("Usain Bolt is not a Racing Athlete.")


