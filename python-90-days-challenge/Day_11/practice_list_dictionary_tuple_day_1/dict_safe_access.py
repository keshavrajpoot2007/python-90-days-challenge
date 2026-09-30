playlist = {"Mockingbird": "Eminem", "Blinding Lights": "The Weeknd", "Shape of You": "Ed Sheeran"}

# Safe access
try:
    playlist["Darkside"]
except KeyError:
    print("Song not found in playlist.")
    
# Using .get(key, default_value_if_not_found)
print(playlist.get("Darkside","Song not found in playlist."))