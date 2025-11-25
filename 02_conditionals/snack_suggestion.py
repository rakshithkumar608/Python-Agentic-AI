# A local cafe wants a program that suggests a snack.
# if a customer asks for cokies or samosa, it confirms the order.
# Otherwise, it says it's not available.


# Task:
# * Take Snack input
# * if it's "cookies" or "samosa", confirm order
# * else, show unavailability



snack = input("Enter your preffered snack: ").lower()

if snack == "cookies" or snack == "samosa":
  print(f"Great Choice! we'll serve you {snack}")
else:
  print("Sorry, we only serve cookies or samosa with tea")
