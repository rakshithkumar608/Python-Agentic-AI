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