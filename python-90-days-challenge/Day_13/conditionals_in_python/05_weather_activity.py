# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input("Hey:), how's the weather (eg. snowy, rainy or sunny): ").lower()
 
if weather == "sunny":
    print("Go for a walk.")
elif weather == "rainy":
    print("Read a Book.")
elif weather == "snowy":
    print("Build a Snowman")
else:
    print("Read the weather name :(")