# ==========================================
# Challenge 1: The Ranking System (enumerate)
# ==========================================
# Problem: You have a list of top anime. Use the enumerate() function to print 
# each anime with its rank. The ranking should start from 1, not 0.

# top_anime = ["Death Note", "Naruto", "One Piece", "AOT"]

# '''
# Expected Output:
# Rank 1 is Death Note
# Rank 2 is Naruto
# Rank 3 is One Piece
# Rank 4 is AOT
# '''

# Write your code below:

# enumerate

top_anime = ["Death Note", "Naruto", "One Piece", "AOT"]

for index, value in enumerate(top_anime, start=1):
    print(f"Rank {index} is {value}")

