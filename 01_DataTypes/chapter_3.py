#Integer

black_coffee_grams = 13
ginger_grams = 2

total_grams = black_coffee_grams + ginger_grams
print(f"Total grams of coffee and ginger: {total_grams}g")


remaining_grams = black_coffee_grams - ginger_grams
print(f"Remaining grams after adding ginger: {remaining_grams}g")

milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(f"Milk for srving is {milk_per_serving}liters")


total_tea_bags = 8
pots = 3
bags_per_pot = total_tea_bags // pots
print(f"Each pot gets : {bags_per_pot} tea bags")


total_cadamon_bags  = 14
pods_per_cup = 3
leftover_pods = total_cadamon_bags % pods_per_cup
print(f"Leftover pods after making cups of tea: {leftover_pods} pods")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"Powerful flavor strength: {powerful_flavor}")
# 2 * 2 * 2 = 8

total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")