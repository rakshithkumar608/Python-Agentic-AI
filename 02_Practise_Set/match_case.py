# 1. Write a program that takes a number (1–7) and prints the day of the week using match-case.

day_number = int(input("Enter a number (1-7) to get the corresponding day of the week: "))

match day_number:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thuesday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday") 
  case _:
    print("Invalid")
          
# 10. Input marks and print Grade using match-case:

grade = input("Enter grade (A+, A, B, C, F): ")

match grade:
    case "A+":
        print("Excellent")
    case "A":
        print("Very Good")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")



# 3. Create a menu using match–case:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide

print("1.Add  2.Subtract  3.Multiply  4.Divide" )

choice = int(input("Enter your choice :"))

a = int(input("Enter first number: "))
b = int(input("Enter Second number:"))

match choice:

  case  1:
    print("Addition of  numbers: ", a+b)
  case 2:
    print("Subtraction of numbers:", a-b)
  case 3:
    print("Multiplication of numbers:", a*b)
  case 4:
    print("Division of numbers:", a/b)
  case _:
    print("Invalid Choice")


# 4. Input month number (1–12). Use match-case to print month name.

months = int(input("Enter the month number (1-12): "))

match months:
  case 1:
    print("January")
  case 2:
    print("February")
  case 3:
    print("March")
  case 4:
    print("April")
  case 5:
    print("May")
  case 6:
    print("June")
  case 7:
    print("July")
  case 8:
    print("August")
  case 9:
    print("September")
  case 10:
    print("October")
  case 11:
    print("November")
  case 12:
    print("December")

    

# 5. Use match-case to print traffic rules:
# red → Stop
# yellow → Wait
# green → Go

color = input("Enter the traffic light color (red, yellow, green): ").lower()
match color:
  case "red":
    print("Stop")
  case "yellow":
    print("Wait")
  case "green":
    print("Go")

# 6. Use match-case:
# 0 → Zero
# 1 → One
# 2 → Two
# 3 → Three
# ...
# 9 → Nine

numbers = int(input("Enter a number (0-9):"))

match numbers:
  case 0:
    print("Zero")
  case 1:
    print("One")
  case 2:
    print("Two")
  case 3:
    print("Three")
  case 4:
    print("Four")
  case 5:
    print("Five")
  case 6:
    print("Six")
  case 7:
    print("Seven")
  case 8:
    print("Eight")
  case 9:
    print("Nine")


# 7. Create a program using conditional statements:
# Calculate electricity bill
# ≤ 100 units → ₹5/unit
# 101–300 → ₹8/unit
# 300 → ₹10/unit


units = int(input("Enter the number of electricity units consumed:"))
match units:
  case units if units <= 100:
    bill = units * 5
    print("Electricity bill is: ₹", bill)
  case units if 101 <= units <= 300:
    print("Electricity bill is: ₹", units * 8)
  case units if units > 300:
    print("Electricity bill is: ₹", units * 10)

#  OR using if-elif-else

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 8
else:
    bill = units * 10

print("Total Bill: ₹", bill)


# 8. Input salary and print tax percentage depending on range.

income = float(input("Enter your annual income: "))

if income <= 2.5:
  print("No Tax")
elif income <= 5:
  print("Tax = 5%")
elif income <= 10:
  print("Tax = 20%")
else:
  print("Tax = 30%")


# 9. Greeting using match-case

time = int(input("Enter time (0-23): "))

match time:
    case t if 0 <= t <= 11:
        print("Good Morning")
    case t if 12 <= t <= 17:
        print("Good Afternoon")
    case t if 18 <= t <= 23:
        print("Good Evening")
    case _:
        print("Invalid Time")


# 10. Food Menu

food = input("Enter food item: ").lower()

match food:
    case "pizza": print("Price: ₹150")
    case "burger": print("Price: ₹80")
    case "fries": print("Price: ₹50")
    case "biryani": print("Price: ₹160")
    case "coke": print("Price: ₹40")
    case _: print("Not available")
   

# 11. Order Status

status = input("Enter order status: ").lower()

match status:
    case "ordered": print("Order Placed")
    case "packed": print("Order Packed")
    case "shipped": print("Shipped")
    case "out_for_delivery": print("Out for Delivery")
    case "delivered": print("Delivered")
    case "cancelled": print("Order Cancelled")
    case _: print("Invalid status")   