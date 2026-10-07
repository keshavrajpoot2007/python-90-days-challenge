s1 = "Hello"
s2 = s1
s1 = s1 + "world"

print(id(s1))
print(id(s2))
print(s1 is s2)
# the output is false beacause when s1 add "world",at that time python create new object that contain "Hello World".