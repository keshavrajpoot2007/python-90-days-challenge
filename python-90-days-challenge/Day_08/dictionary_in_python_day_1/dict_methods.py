sports_players = {"Cricket": "Virat Kholi", "Football": "Cristiano Ronaldo", "Racing": "Usain Bolt"}
print(sports_players)

# Find length of dictionary
print("Length: ", len(sports_players)) # Output: 3, because key and value count as a single element in dictionary.

# Access all Keys of Dictionary using key()
print(sports_players.keys())

# Access all value of Dictionary using value()
print(sports_players.values())

# Copy Dictionary using copy()
sports_players_copy = sports_players.copy() 
print("Copy Dictionary: ", sports_players_copy)
print(sports_players_copy is sports_players) # Output: False

# Clear dictionary using clear

sports_players.clear()
print("sports_players: ", sports_players)

