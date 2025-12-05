#1. Print multiplication table of any given number

# n = int(input("Enter a number:"))

# for i in range(1, 11):
#   print(n, "x", i, "=", n * i)


#2. Print Fibonacci series up to n 

# n = int(input("Enter limit:"))
# a,b = 0, 1

# print(a, b, end= " ")

# for _ in range(n - 2):
#   c = a + b
#   print(c, end=" ")
#   a = b
#   b = c



# 3.Print all prime numbers between 1 and 200

for num in range(2, 201):
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")


# Print star pattern
# *
# **
# ***
# ****
# *****


for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


for i in range(1, 6):
    x = 1
    while(x<=i):
       print(x, end="")
       x += 1
    print()

for i in range(1, 6):
    x = 1
    while(x<=i):
        print("*", end="")
        x += 1
    print()


lower = int(input("Enter a lower limit:"))
upper = int(input("Ebter a upper limit:"))

num = lower
print("Prime numbers:")

while num <= upper:
    if num > 1:
        i = 2
        is_prime = True
        while i < num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(num, end=" ")
    num += 1