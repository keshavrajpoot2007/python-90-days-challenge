# -----------Any of these function doesn't change the original string, because string is immutable. They just return a new string. They create a new object in memory.-----------



# Case Conversion
## .upper() and .lower()

Anime = "Attack on Titan"

Upper_Case_Anime = Anime.upper() # Store Anime value in CAPITAL letter into Upper_Case_Anime.
Lower_Case_Anime = Anime.lower() # Store Anime value in small letter into Lower_Case_Anime.

print(Upper_Case_Anime) # Output: ATTACK ON TITAN
print(Lower_Case_Anime) # Output: attack on titan

print(Anime.upper()) # Output: ATTACK ON TITAN, It doesn't change the original string, instead it generates a new object in memory with the converted value.

print(Anime) # Output: Attack on Titan

## isupper() and islower()
### Check letters are capital or small.

print(Upper_Case_Anime.isupper()) # Output: True
print(Lower_Case_Anime.islower()) # Output: True
print(Anime.islower()) # Output: False
print(Anime.isupper()) # Output: False


# ------------------------------------------------------------------------------------------------------



# Removing Whitespaces
# .strip() - remove space from front and back of string

Movie = "        365 days       "

print(Movie) # Output:         365 days       
print(Movie.strip()) # Output: 365 days



# ------------------------------------------------------------------------------------------------------


# Replace 

Series = "Game of Thrones"
New_Series = Series.replace("Thrones", "Throne") # Replace Thrones with Throne in Series and store the new value into New_Series.   

print(Series) # Output: Game of Thrones
print(New_Series) # Output: Game of Throne



