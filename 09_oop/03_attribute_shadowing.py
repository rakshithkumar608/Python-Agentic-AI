class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(f"The temperature of cutting chai: {cutting.temperature}")

cutting.temperature = "Warm"
cutting.cup = "small"
print(f"The temperature of cutting chai: {cutting.temperature}")
print("Direct look into the class", Chai.temperature)
print(f"The cup of cutting chai: {cutting.cup}")
# print(f"The strength of cutting chai: {cutting.strength}")

del cutting.temperature
del cutting.cup
print(f"The temperature of cutting chai: {cutting.temperature}")
print(f"The cup of cutting chai: {cutting.cup}")
