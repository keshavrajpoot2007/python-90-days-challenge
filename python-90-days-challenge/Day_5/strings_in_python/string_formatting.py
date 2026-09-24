# String Formatting
# .format() - dynamically inserts variables into placeholders {} inside a string


Superhero = "Batman"
City = "Gotham"
Villain_Count = 5


# Using .format() with empty placeholders {}

Dialogue_1 = "I am {}, and I protect {}.".format(Superhero, City)


# Using .format() with index numbers {0}, {1}

Dialogue_2 = "{0} has defeated {1} villains in {2} tonight.".format(Superhero, Villain_Count, City)


# Changing the order using index numbers

Dialogue_3 = "Welcome to {2}. {0} is watching. Total villains caught: {1}.".format(Superhero, Villain_Count, City)


print("String Formatting using .format():")
print("Dialogue_1:", Dialogue_1) # Output: I am Batman, and I protect Gotham.
print("Dialogue_2:", Dialogue_2) # Output: Batman has defeated 5 villains in Gotham tonight.
print("Dialogue_3:", Dialogue_3) # Output: Welcome to Gotham. Batman is watching. Total villains caught: 5.
print("\n")