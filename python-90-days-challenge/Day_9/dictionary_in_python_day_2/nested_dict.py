# <------------------------------- Nested Dictionary ------------------------------->

tea_shop = {
"chai": {"Masala": "Spicy", "Ginger": "Zesty"},
"Tea": {"Green": "Mild", "Black": "Strong"}
}

print("Tea Shop: ", tea_shop)
# Output: Tea Shop:  {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}


# <-------------------- Access keys and value of Nested Dictionary -------------------->

# 1. Access inside Dictionary
print(tea_shop["chai"]) # Output: {'Masala': 'Spicy', 'Ginger': 'Zesty'}

# 2. Access value of inside Dictionary
print(tea_shop["chai"]["Ginger"]) # Output: Zesty

# 3. Add values
tea_shop["Tea"]["Masala"] = "Tikhi"
print(tea_shop) # Output: {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong', 'Masala': 'Tikhi'}}

# 4. Remove value
del tea_shop["Tea"]["Masala"]
print(tea_shop) # Output: {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}

# 5. Update values
tea_shop["chai"]["Masala"] = "Tikhi"
print(tea_shop) # Output: {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}

# 6. Update nested dictionary
tea_shop["chai"] = {"Kali": "Majboot", "Hari": "halki"}
print(tea_shop) # Output: {'chai': {'Kali': 'Majboot', 'Hari': 'halki'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}

# 7. clear nested dictionary
tea_shop["chai"].clear()
print(tea_shop) # Output: {'chai': {}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}