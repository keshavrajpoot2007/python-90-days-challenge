import math

floor_test_positive_number = 2.8
floor_test_negative_number = -3.4

trunc_test_positive_number = 2.8
trunc_test_negative_number = -3.4

print(math.floor(floor_test_positive_number)) # Output: 2, because floor returns the lest intiger number from float.
print(math.floor(floor_test_negative_number)) # Output: -4, because -4 is less than 3.8 .

print(math.trunc(trunc_test_positive_number)) # Output: 2, because trunc return integer that is closer to 0.
print(math.trunc(trunc_test_negative_number)) # Output: -3, because -3 is closer to 0.
