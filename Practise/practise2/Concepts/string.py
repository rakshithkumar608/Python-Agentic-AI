name = input("Enter your name:")

while name == "":
  print("Name cannot be empty")
  name = input("Enter youe name:")

email = input("Enter the Email :")

while "@" not in email or "." not in email:
  print(f"Invalid email. Please enter again.")
  email = input("Enter the correct Email :")


phone = input("Enter your phone number:")

while len(phone) != 10 or not phone.digit():
  print("Enter 10 digits phone number")
  phone = input("Enter your phone number:")


print("Form submitted succesfully")



