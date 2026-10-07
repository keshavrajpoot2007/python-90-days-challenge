# Dictionary contain two things:
#       Key - in dictionary we dont have index, we make our key values for accesing elements.
#       value - each key consist a value in dictionary
#       dict_name = {"Key": "value"}

# **(Note - python make object of each value in memory, and the reference of these object are store in key.)**

emotions_reactions = {"sad": "cry", "happy": "laugh", "angry": "shout"} # Dictionary created, name emotions_actions

print("Emotions and there sudden reactions: ", emotions_reactions)



# <-------------------- for explaning behind the scene working -------------------->

emotions_reactions["happy"] = "cry" # put cry value in happy key, same value as sad

# Now we check, is the cry same for sad and happy or different?.

print(emotions_reactions["happy"] == emotions_reactions["sad"]) # Output: True, because values are same(cry)

print(emotions_reactions["happy"] is emotions_reactions["sad"])# Output: True, because locations are also same
                                                  
print(f"Happy cry location: {id(emotions_reactions["happy"])} \nSad cry loction: {id(emotions_reactions["sad"])}")
# Output: Happy cry location: 137972210600480 
# Output: Sad cry loction: 137972210600480

