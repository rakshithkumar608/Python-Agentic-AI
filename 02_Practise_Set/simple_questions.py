# 1. Input a number. Check if it is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
  print(f"{number} is Even Number")
else :
  print(f"{number} is Odd Number")


# 2. Ask the user’s age and print:
# If age ≥ 18 → Eligible to vote
# Else → Not eligible 

voter_age = int(input("Enter your age:"))
if voter_age >= 18:
  print(f"You are eligible to vote")
else:
  print(f"You are not eligible to vote")


# 3. Input two numbers, print the largest.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)


# 4. Input a number and print whether it is positive, negative, or zero.

a = int(input("Enter a number:"))

if a > 0:
  print(f"{a} is a positive number")

elif a < 0:
  print(f"{a} is a negative number")
else:
  print("The number is zero")


# 5. Input 3 subject marks, calculate percentage and print:

# ≥ 90 → A+

# ≥ 75 → A

# ≥ 60 → B

# ≥ 35 → C

# < 35 → Fail

subject_1 = int(input("Enter marks of subject 1:"))
subject_2 = int(input("Enter marks of subject 2:"))
subject_3 = int(input("Enter marks of subject 3:"))


total = subject_1 + subject_2 + subject_3
print(f"The total marks of the 3 subjects: {total}")
percntage = (total / 300) * 100
print(f"The percentage: {percntage}")

if percntage >= 90:
  print("Grade: A+")
elif percntage >= 75:
  print("Grade: A")
elif percntage >= 60:
  print("Grade: B")
elif percntage >= 35:
  print("Grade: C")
elif percntage < 35:
  print("Grade: Fail")


# 6. Input a year and check whether it is a leap year or not.


year = int(input("Enter a year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print("Leap year")
else:
  print("Not a Leap year")


# 7. Input a character and check if it is vowel or consonant.

ch = input("Enter a character:").lower()

if ch in "aeiou":
  print(f"{ch} is a Vowel")
else:
  print(f"{ch} is a Consonant")


# 8. Input a password and check if it matches "python123".
# Print Login successful or Invalid password.


pwd = input("Enter your password:")
if pwd == "python123":
  print("Login successful")
else:
  print("Invalid password")


# 9. ATM: Input balance & withdrawal amount. If enough balance, deduct, else display Insufficient balance.

balance = float(input("Enter your account balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount:"))

if withdrawal_amount <= balance:
  balance -= withdrawal_amount
  print(f"withdrawal successful. New balance is: {balance}")
else:
  print("Insufficient balance")