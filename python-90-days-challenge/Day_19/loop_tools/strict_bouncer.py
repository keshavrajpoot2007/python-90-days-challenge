# ==========================================
# Challenge 4: The Strict Bouncer (filter)
# ==========================================
# Problem: You have a list of user ages. Use the filter() function or a List 
# Comprehension to create a new list that only contains ages of adults (18 or older).

# user_ages = [12, 18, 25, 9, 30, 16]

# '''
# Expected Output:
# [18, 25, 30]
# '''

# Write your code below:

user_ages = [12, 18, 25, 9, 30, 16]

converted = filter(lambda x: x >= 18, user_ages)

new_list = list(converted)

print(new_list)