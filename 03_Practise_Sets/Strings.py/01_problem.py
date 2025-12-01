# Check if a string is a palindrome (ignore spaces & case).

text = input("Enter a String:")

cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
  print("It's a Palindrome")
else:
  print("It's not a Palindrome")