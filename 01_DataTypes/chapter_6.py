chai_type = "Black Tea" # String variable to hold the type of chai
customer_name = "Raj"

print("Welcome to the Tea Shop!")
print(f"Hello {customer_name}, your order for {chai_type} is being prepared.")


# String Slicing 
chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:6]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}")


# Encoding Example
label_text = "Chai Special"
encoded_label = label_text.encode('utf-8')
print(f"Original label : {label_text}")
print(f"Encoded label : {encoded_label}")

decoded_label = encoded_label.decode('utf-8')
print(f"Decoded label : {decoded_label}")