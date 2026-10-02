# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pat_species = input("Which pat you have? (eg. dog or cat)- ").lower()

if pat_species == "dog" or pat_species == "cat":
    
    pat_age = int(input("How old your pat is? - "))
    
    if pat_species == "dog" and pat_age < 2:
        food = "Puppy food"
    
    elif pat_species == "cat" and pat_age > 5:
        food = "Senior cat food"
        
    else:
        print(f"We don't have any data for {pat_species} of this age group.")
        exit()
else:
    print(f"We don't have any data for {pat_species}.") 
    exit() 
    
print(f"You feed {food} to your {pat_species}.")