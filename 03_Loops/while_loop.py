# You want to simulate tea heating.
# It starts at 40C and boils at 100c

# Task:
# *Use a while loop.
# *Increase temperature by 15 until it reaches or exceeds 100.
# *Print each temperature step.

temp = 40

while temp < 100:
  print(f"Current temperature: {temp}")
  # temp = temp + 15
  temp += 15

print("Tea is ready to boil")