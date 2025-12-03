# Print the sum of digits of a number. (Example: 451 → 4+5+1 = 10)

n = int(input("Enter The numbers:"))
total = 0
while n > 0:
  total += n % 10
  n //= 10
  print(f"Sum:{total}")

# Check if a number is prime using a loop.

n = int(input("Enter a no to check Prime or Not:"))
isPrime = True

if n < 2:
    isPrime = False
else:
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break

print("Prime" if isPrime else "Not Prime")


# Print numbers from 1 to 100, but skip multiples of 3.

for i in range(1, 101):
  if i % 3 == 0:
    continue
  print(f"The numbers:{i}")

# Find the largest number in a list using a loop (no max()).

nums = [3, 8, 1, 9, 6]
maxi = nums[0]
for n in nums:
    if n > maxi:
        maxi = n
print(f"The max number is:{maxi}")


# Count vowels and consonants in a string.

s = input("Enter the string:").lower()
vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# Print all odd numbers in reverse order from 99 to 1.

for i in range(90, 0, -2):
  print(i)


# Keep taking input from user until they enter 0, then print the sum of all numbers.

total =0
while True:
  n = int(input("Enter number:"))
  if n == 0:
    break
  total += n
  print(f"Total = {total}")

# Display numbers from a list that are greater than the average of the list.

nums = [10, 20, 30, 40, 50]
avg = sum(nums) / len(nums)
for n in nums:
    if n > avg:
        print(n)


# Print a string in reverse without using slicing.

s = input("Enter the String:")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)


# Generate this output using loops:

for i in range(1, 6):
    print("*" * i)
