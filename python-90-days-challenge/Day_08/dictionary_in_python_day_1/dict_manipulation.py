emotions_reactions = {"sad": "cry", "happy": "laugh", "angry": "shout"}
print("Dictionary emotions_reactions: ", emotions_reactions)

# <------------------------------- Dictionary Manipulation ------------------------------->

# 1. Access elements

## using salicing
element = emotions_reactions["angry"]
print(f"{element} is an angry reaction.")

## using get()
emotions_reactions.get("happy")

# 2. Replace key values
emotions_reactions["angry"] = "punch"
print("After R=replcing angry: ", emotions_reactions)

#3. Add new element
emotions_reactions["tired"] = "rest"
print("After adding new element: ", emotions_reactions)

# 4. Delete element

## using pop()
emotions_reactions.pop("angry")
print("After remove angry: ", emotions_reactions)

## using popitem()
emotions_reactions.popitem() # remove last element
print("After remove last element: ", emotions_reactions)

## using del
del emotions_reactions["happy"]
print("After deleting happy: ", emotions_reactions) # it deletes from the memory

