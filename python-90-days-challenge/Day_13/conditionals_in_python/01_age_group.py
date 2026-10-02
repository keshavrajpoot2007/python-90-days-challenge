# Problem: Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input("Enter Your age: "))

if age < 13:
  print("You are a Child.")

elif age < 20: 
  print("You are a Teenager.")
    
elif age < 60: 
  print("You are an Adult.")
    
else:
  print("You are a Senior.")