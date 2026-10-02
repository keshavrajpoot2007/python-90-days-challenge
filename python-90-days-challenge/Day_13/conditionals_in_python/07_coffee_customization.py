# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Tell your coffee order sir! (Small, Medium or Large): ").capitalize()
extra_short = input(f"Are you want your {order_size} espresso with extra short sir? (y/n): ").lower()

if extra_short == "y":
    coffee = order_size + " Extra Short Espresso"
else:
    coffee = order_size + " Espresso"
    
print("Take your",coffee)