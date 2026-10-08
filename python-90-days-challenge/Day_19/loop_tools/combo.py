# ==========================================
# Challenge 5: The Boss Level Combo (zip + if)
# ==========================================
# Problem: Iterate through both tech_companies and stock_prices simultaneously 
# using zip(). Print the company name and its price ONLY IF the stock price 
# is strictly less than 200.

# tech_companies = ["Apple", "Google", "Microsoft", "Netflix"]
# stock_prices = [150, 2800, 310, 90]

# '''
# Expected Output:
# Apple stock price is 150
# Netflix stock price is 90
# '''

# Write your code below:


tech_companies = ["Apple", "Google", "Microsoft", "Netflix"]
stock_prices = [150, 2800, 310, 90]

for company, price in zip(tech_companies, stock_prices):
    if price < 200:
        print(f"{company} stock price is {price}")