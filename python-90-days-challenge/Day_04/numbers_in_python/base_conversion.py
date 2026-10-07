# 0o - Octal
# 0x - Hexadecimal
# 0b - Binary

print(0o64) # Output: 52, Decimal value of oOtal 64 is 52.
print(0xFF) # Output: 255, Decimal value of Hexadecimal FF is 255.
print(0b0101) # Output: 5, Decimal value of Binary 0101 is 5.

# Conversion in octal from other number systems by oct() method.

print(oct(52)) # Decimal to Octal.
print(oct(0x7A8B)) # Hexa to Octal.
print(oct(0b10001)) # Binary to Octal.

# Conversion in Hexadecimal from other number systems by hex() method.

print(hex(52)) # Decimal to Hexa.
print(hex(0o76)) # Octal to Hexa.
print(hex(0b100011)) # Binary to Hexa.

# Conversion in binary from other number systems by bin() method.

print(bin(100)) # Decimal to binary.
print(bin(0o57)) # Octal to binary.
print(bin(0xABCD)) # hexa to binary.

# Conversion in Decimal from other number systems by bin() method.

print(int(100)) # Binary to Decimal.
print(int(0o57)) # Octal to Decimal.
print(int(0xABCD)) # Hexa to Decimal.

# Conversion in Decimal from any other base, without 0b, 0x, 0o by bin() method.

print(int('67', base=8)) # Base 8
print(int('69', base=16)) # Base 16
print(int('11', base= 2)) # Base 2
print(int('55', base=6)) # Base 6
print(int('123', base=20)) # Base 20
print(int('33', base=4)) # Base 4