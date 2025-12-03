# Print multiplication tables from 1–10 using nested loops.

for i in range(1, 11):
  for j in range(1, 11):
    print(i, "x", j, "=", i*j)
    print()

# Print all prime numbers between 1 and 300.

for n in range(2, 301):
  isPrime = True

  for i in range(2, n):
    if n % i == 0:
      isPrime = False
      break
  if isPrime:
    print(n)

# Print a pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(1, 5):
    for j in range(1, i+1):
     print(j, end=" ")
    print()

# Print an inverted pattern:

# *****
# ****
# ***
# **
# *

for i in range(5, 0, -1):
    print("*" * i)

# Create a number pyramid:

#     1
#    2 2
#   3 3 3
#  4 4 4 4

for i in range(1, 5):
    print(" " * (5-i), end="")
    for j in range(i):
      print(i, end=" ")
    print()

# Check if a string is palindrome using loops (e.g., "level").

s = input("Enter a string:")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Its Palindrome")
else:
    print("Not a Palindrome")


# Find the GCD of two numbers using loops.

a = int(input("Enter first no:"))
b = int(input("Enter second no:"))

while b != 0:
   a,b = b, a%b
print("GCD = ", a)

# Bubble sort logic using loops (no sort() allowed).

a = [5,2,8,9,6]

for i in range(len(a)):
    for j in range(0, len(a)-i-1):
        if a[j] > a[j+1]:
           a[j], a[j+1] = a[j+1], a[j]
print(a)

# Print this pattern:

# A
# B C
# D E F
# G H I J

ch = 65
for i in range(1, 8):
    for j in range(i):
      print(chr(ch), end=" ")
      ch += 1
    print()


# Print all Armstrong numbers between 1 and 1000 (e.g., 153, 370, 371).

for n in range(1, 1001):
   num = n
   s = 0
   while num > 0:
      d = num % 10
      s += d ** 3
      num //= 10
   if s == n:
    print(n)