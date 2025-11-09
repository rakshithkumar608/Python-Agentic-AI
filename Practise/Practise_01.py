# Smart Password Strength Analyzer Using Strings, Slicing, Encoding, Booleans, Numbers, and Operators

password = input("Enter your password: ")

# ----- Basic information -----
length = len(password)
first_part = password[:3]
last_part = password[-3:]

# --- Initialize flags ---
has_upper = False
has_lower = False
has_digit = False
has_special = False

# --- Analyze each character ---
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

# --- Encoding (ASCII sum) ---
ascii_sum = sum(ord(ch) for ch in password)

# -------- Defining Strength --------
if length >= 8 and has_upper and has_lower and has_digit and has_special:
    strength = "STRONG ✅"
elif length >= 6 and (has_upper or has_lower) and (has_digit or has_special):
    strength = "MEDIUM ⚠️"
else:
    strength = "WEAK ❌"

# ---- Suggestions to improve ----
suggestions = []
if length < 8:
    suggestions.append("Increase password length to at least 8 characters.")
if not has_upper:
    suggestions.append("Add at least one Uppercase Letter (A-Z).")
if not has_lower:
    suggestions.append("Add at least one Lowercase Letter (a-z).")
if not has_digit:
    suggestions.append("Include at least one number (0-9).")
if not has_special:
    suggestions.append("Include at least one special character (e.g., !, @, #, $).")

# ------ Output ------
print("\nPassword Analysis:")
print(f"- Length: {length}")
print(f"- Starts with: {first_part}")
print(f"- Ends with: {last_part}")
print(f"- Contains Uppercase: {has_upper}")
print(f"- Contains Lowercase: {has_lower}")
print(f"- Contains Number: {has_digit}")
print(f"- Contains Special Character: {has_special}")
print(f"- ASCII Sum: {ascii_sum}")
print(f"\nPassword Strength: {strength}")

if suggestions:
    print("\n Suggestions to improve your password:")
    for s in suggestions:
        print("• " + s)
else:
    print("\n✅ Great job! Your password is strong and secure.")
