a = 100
b = 100

print(id(a))
print(id(b))
print(a is b)

# Output is True in both shell and file, because python saves small numbers from -5 to 256 in memory by default. so when we assign a small number, python gives the reference of already saved number instead of making new one. So 100 is under cache range.