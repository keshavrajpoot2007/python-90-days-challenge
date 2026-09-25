# Base Calculator is use to calculate the numbers acording to there base.

print("Enter Two octal numbers:- ")
int_num1 = int(input("Enter First Number: "), base = 8)
int_num2 = int(input("Enter Second Number: "), base = 8)
print("\n")

# Covert
num1 = oct(int_num1)
num2 = oct(int_num2)


# Calculate answer and store in integer format.
addition = int_num1 + int_num2
substraction = int_num1 - int_num2
divison = int_num1 / int_num2
multiplication = int_num1 * int_num2
power = int_num1 ** int_num2


print("Octal Answers:")
print(f"{int_num1:o} + {int_num2:o} = {addition:o}") 
print(f"{int_num1:o} - {int_num2:o} = {substraction:o}") 
print(f"{int_num1:o} * {int_num2:o} = {multiplication:o}") 
print(f"{int_num1:o} ** {int_num2:o} = {power:o}") 
print("\n")
# <-----------------------------------------Error----------------------------------------->
# print(f"{int_num1:o} - {int_num2:o} = {divison:o}") 
# -------ValueError: Unknown format code 'o' for object of type 'float'-------

# oct_div = oct(divison)
# -------TypeError: 'float' object cannot be interpreted as an integer-------

# we can solve this problem by making own function of coverting floating values in octal
# <-----------------------------------------Error----------------------------------------->

print("Decimal conversion of given values and answer:")
print(int_num1, " + ", int_num2, " = ", addition)
print(int_num1, " - ", int_num2, " = ", substraction)
# print(int_num1, " / ", int_num2, " = ", divison)
print(int_num1, " * ", int_num2, " = ", multiplication)
print(int_num1, " ^ ", int_num2, " = ", power)





