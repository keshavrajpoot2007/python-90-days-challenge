# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)


fruit = input("Enter fruit (eg. Banana): ")
color = input("Enter color (Yellow, Green or Brown): ")

# if color == "Yellow" or color = "yellow" or color = "YELLOW": # always write full conditon after 'or' otherwise it make the other condition unreachable.  
if fruit in ["Banana", "banana", "BANANA"]:

    # if color == "Yellow" or color == "yellow" or color == "YELLOW":
    if color in ["Yellow", "yellow", "YELLOW"]:
        print("Ripe")
        
    # elif color == "Green" or color == "green" or color == "GREEN":
    elif color in ["Green", "green", "GREEN"]:
        print("Unripe")
        
    # elif color == "Brown" or color == "brown" or color == "BROWN":
    elif color in ["brown", "Brown", "BROWN"]:
        print("Overripe")
    else:
        print("Invalid Color")
        
else:
    print("Currently we dont have information of this fruit.")