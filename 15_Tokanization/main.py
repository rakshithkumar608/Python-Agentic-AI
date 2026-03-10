import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Rakshith Kuamr"
tokens = enc.encode(text)

# Token [25216, 3274, 0, 3673, 1308, 382, 69387, 1116, 437, 23393, 313, 81]
print("Token", tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 69387, 1116, 437, 23393, 313, 81])
print("Decoded Tokens:", decoded)