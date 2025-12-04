password = input("Enter a password:")

has_lower = False
has_upper = False
has_digits = False
has_special = False
special_char = "@#$&"

if len(password) >= 6:
  for ch in password:
    if ch.islower():
      has_lower = True
    elif ch.isupper():
      has_upper = True
    elif ch.isdigit():
      has_digits = True
    elif ch in special_char:
      has_special = True
    else:
      print("Invalid Password: Minimum length should be 6")
      exit()
if has_lower and has_upper and has_digits and has_special:
  print("Valid password")
else:
  print("Invalid password")
    
