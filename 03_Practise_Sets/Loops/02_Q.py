# 1. Print numbers from 1 to 50 using a loop.

for num in range(1, 51):
  print(f"The Numbers :{num}")

# 2.Print even numbers between 1 to 100.

for i in range(2, 101, 2):
  print(f"The even no:{i}")


#3. Print the multiplication table of a given number n.

n = int(input("Enter number:"))
for i in range(1,11):
  print(n, "x",i, "=", n * i)

#4.Print the sum of numbers from 1 to n.
n = int(input("Enter n:"))
total = 0
for i in range(1, n+1):
  total += 1
  print("Sum =", total)

#5. Print all numbers divisible by 5 between 1 and 200.

for i in range(1, 201):
  if i % 5 == 0:
    print(f"The divisible of 5 is:{i}")

# 6.Count how many digits are in a given number (using while loop).

n = int(input("Enter number:"))
count = 0
while n > 0:
  count += 1
  n //= 10
  print("Digits:", count)

# Reverse a number using a loop (e.g., 123 → 321).

n = int(input("Enter a number to reverse:"))
rev = 0
while n > 0:
  r = n % 10
  rev = rev * 10 + r
  n //= 10
  print(f"Reversed: {rev}")

# Print the factorial of a given number.

n = int(input("Enter a Factorial number:"))
fact = 1
for i in range(1, n+1):
  fact *= i
  print(f"Factorial:{fact}")


# Print the first 10 Fibonacci numbers.
a, b = 0, 2
for i in range(10):
  print(a)
  a,b = b, a+b

# Print characters of a string one by one, each on a new line

s = input("Enter a String:")
for ch in s:
  print(f"The String:{ch}")
