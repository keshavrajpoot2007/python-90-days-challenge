orignal_list = [1, 2, 3]
clone_list = orignal_list[:]

print(orignal_list)
print(clone_list)

orignal_list[0] = 55

print(orignal_list) #output: [55, 2, 3]
print(clone_list) #output: [1, 2, 3], because if we use slicing(:) then python create a copy of refernce instead of giving same reference.

# Another Method for copy list.
import copy

clone_list = copy.copy(orignal_list) 

print(clone_list)
