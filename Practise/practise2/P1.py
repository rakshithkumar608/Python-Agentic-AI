# 1️⃣ Reverse a string (SLICING)

s = "python"

rev = s[::-1]
print(rev)

# 2️⃣ Count vowels in a string
s = "education"
vowels = "aeiou"
count = 0

for ch in s:
  if ch in vowels:
    count += 1
print(count)


# 3️⃣ Remove duplicates from a list (USING SET)
l = [1,2,1,3,4,3,2,1,5]

r = list(set(l))
print(r)

# 4️⃣ Find largest number (NO max())

l = [10,30,50,67]

largest = l[0]
for num in l:
  if num > largest:
    largest = num
print(largest)

# 5️⃣ Palindrome check

s = "madam"

if s == s[::-1]:
  print(True)
else:
  print(False)


# 6️⃣ Character frequency (IMPORTANT)

s = "Rakshith"
freq = {}

for ch in s:
  freq[ch] = freq.get(ch,0) + 1

print(freq)

# 7️⃣ Common elements between two lists

a = [1, 2,3,4,5]
b = [2,4,6,3,1,8]

common = set(a) & set(b)
print(common)

# 8️⃣ Create dictionary from two lists

keys  = ["names", "age", "city"]
values = ["Ravi", 21, "Banglore"]

result = dict(zip(keys, values))
print(result)


# 9️⃣ Remove even numbers

l = [1, 2, 3, 4, 5, 6]
result = []

for num in l:
  if num % 2 !=0:
    result.append(num)

print(result)


# 🔟 Second largest number

l = [10,20,40,50]

l.sort()
print(l[-2])




s = "rakshith"

rev = s[::-1]
print(rev)


a = "rakshith"


freq = {}
for ch in a:
  freq[ch] = freq.get(ch,0) + 1

print(freq)

l = [23,70,50]

l.sort()
print(l[-2])

l = [23,70,60]

largest = second = -1

for num in l:
  if num > largest:
    second = largest
    largest = num
  elif num > second and num != largest:
    second = num

print(second)

color = (255, 0, 0)
print(color)