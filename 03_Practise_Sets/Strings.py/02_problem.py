# Count vowels, consonants, digits & special characters

s = input("Enter a string: ")

vowels = "aeiou"
v_count = c_count = d_count = sp_count = 0

for ch in s.lower():
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1
    elif ch.isdigit():
        d_count += 1
    else:
        sp_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
print("Digits:", d_count)
print("Special Characters:", sp_count)

