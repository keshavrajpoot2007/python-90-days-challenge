set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets

## By using the union() method
union_set = set1.union(set2)
print(union_set) # Output: {1, 2, 3, 4, 5}, because union combines all unique elements from both sets.

## By using the | operator
union_set_operator = set1 | set2
print(union_set_operator) # Output: {1, 2, 3, 4, 5}, because | operator also combines all unique elements from both sets.


# Intersection of two sets

## By using the intersection() method
intersection_set = set1.intersection(set2)
print(intersection_set) # Output: {3}, because intersection returns only the elements that are common to both sets.

## By using the & operator
intersection_set_operator = set1 & set2
print(intersection_set_operator) # Output: {3}, because & operator also returns only the elements that are common to both sets.


# Difference of two sets

## By using the difference() method
difference_set = set1.difference(set2)
print(difference_set) # Output: {1, 2}, because difference returns only the elements that are in set1 but not in set2.

## By using the - operator
difference_set_operator = set1 - set2
print(difference_set_operator) # Output: {1, 2}, because - operator also returns only the elements that are in set1 but not in set2.

