name = input("Enter Your First name: ").strip()
surname = input("Enter Your Surname:").strip()

print(f"- Your Full name is {name} {surname}.")
print(f"- Your name length is {len(name+surname)} characters without space.")

reverse_name = surname[::-1] + " " + name[::-1]

print(f"- Your reverse name is {reverse_name}.")

# <-------------------------------------First Attempt------------------------------------->

# Just for Logic Building.
# Succesfull but only in two words name.
# For capital first word of every letter.

# formated_rname =f" {reverse_name[0].upper()}{reverse_name[1:reverse_name.find(" ")].lower()} {reverse_name[reverse_name.find(" ")+1].upper()}{reverse_name[reverse_name.find(" ")+2:].lower()}"

# <-------------------------------------First Attempt------------------------------------->

# <-------------------------------------Second Attempt------------------------------------->

# By .title() - Capitalize the first letter of every word

formated_rname = reverse_name.title()

# <-------------------------------------Second Attempt------------------------------------->

print(f"- Your reverse name in format {formated_rname}")