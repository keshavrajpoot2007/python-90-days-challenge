x = 0.1 + 0.1 + 0.1 - 0.3

print(x) # Output: 5.551115123125783e-17, due to float precison.

from decimal import Decimal

y = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') # Always use string representation to avoid floating-point issues.
print(y) # Output: 0.0, so Decimal solve our float pricison problem.