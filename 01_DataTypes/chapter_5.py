# real numbers



import sys
from fractions import Fraction
from decimal import Decimal


ideal_temp = 95.5
current_temp = 95.99999544599

print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")
print(f"Difference in temp { current_temp - ideal_temp }")
print(sys.float_info)
precise_temp = Decimal('95.99999544599')
print(f"Precise temp { precise_temp }")
print(f"Difference in precise temp { precise_temp - Decimal('95.5') }")