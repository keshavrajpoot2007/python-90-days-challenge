tech_companies = ("Apple", "Google", "Microsoft", "Apple", "Amazon", "Apple")

# Apple count
print(tech_companies.count("Apple"))

# List conversion
tech_companies_list = list(tech_companies)
print(tech_companies_list)

del tech_companies_list[-1]
print(tech_companies_list)

# another way to delete
tech_companies_list.remove("Apple")
print(tech_companies_list)

tech_companies = tuple(tech_companies_list)
print(tech_companies)
