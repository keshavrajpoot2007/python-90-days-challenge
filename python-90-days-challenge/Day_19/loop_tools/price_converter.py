# ==========================================
# Challenge 3: The Price Converter (map)
# ==========================================
# Problem: You have a list of prices in USD. Use the map() function or a List 
# Comprehension to convert all prices to INR (Assume 1 USD = 97 INR). 
# The final result must be a list.

# prices_in_usd = [10, 20, 50, 100]

# '''
# Expected Output:
# [830, 1660, 4150, 8300]
# '''

# Write your code below:

prices_in_usd = [10, 20, 50, 100]


prices_in_usd = [10, 20, 50, 100]

# lambda x: x * 83 ek temporary function hai jo har value ko 83 se multiply karega
converted_map = map(lambda x: x * 83, prices_in_usd)

# Map object ko wapas List mein convert kiya
prices_in_inr = list(converted_map)

print(prices_in_inr)

