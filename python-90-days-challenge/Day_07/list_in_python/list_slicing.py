tech_companies = ["Microsoft", "Google", "Apple", "Amazon"]

# ---------------------------- Acees elements using slicing ----------------------------
 
print("\n Acees elements using slicing:- \n \n")
print("Tech Companies List: ", tech_companies[:]) # Output: ["Microsoft", "Google", "Apple", "Amazon"]
print("Tech Company 2 ", tech_companies[1]) # Output: Google
print("Last Tech Companies: ", tech_companies[-1]) # Output: Amazon
print("Tech Companies 1 to 3: ", tech_companies[0:3]) # Output: ['Microsoft', 'Google', 'Apple']
print("Tech Companies in reverse order: ", tech_companies[::-1]) # Output: ['Amazon', 'Apple', 'Google', 'Microsoft']
print("\n")



# ---------------------------- List Modification using slicing ---------------------------- 


# 1. Changing single element
tech_companies[-1] = "Meta"
print("After replacing last element: ", tech_companies)

# 2. Replacing multiple elements using slice
tech_companies[0:3] = ["OpenAI", "Samsung"]
print("After replacing index 0, 1 and 2: ", tech_companies)

# 3. Inserting elements using empty slice
# This doesn't delete anything, just pushes elements to the right
tech_companies[2:2] = ["Microsoft"] 
print("After inserting at index 2:", tech_companies)
tech_companies[4:4] = ["NVIDA"] 
print("After insertinf at last index: ", tech_companies)

# 4. Deleting elements using empty list assignment
tech_companies[2:4] = []
print("After deleting index 2 and 3:", tech_companies)




