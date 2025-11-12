# Lists (From this here they can be changed this are Mutables)


#Adding the element to list
ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")

#Removing th element from list
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

#Extend the list
car_brands = ["BMW", "Mercedes"]
car_specifications = ["super charged", "petrol"]
car_specifications.extend(car_brands)
print(f"Cars: {car_specifications}")

#Inserting 
car_specifications.insert(2,"drifting") #indexing 
print(f"After adding: {car_specifications}") 
last_added = car_specifications.pop()
print(f"{last_added}")
print(f"After adding: {car_specifications}") 

#reversing list
car_specifications.reverse()
print(f"After revresing: {car_specifications}") 

#sorting list
car_specifications.sort()
print(f"After Sorting: {car_specifications}") 


# levels - Max, Min
sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

#Operator overloading
base_liquid = ["water", "milk"]
extra_flavoure = ["ginger"]

full_liquid_mix = base_liquid + extra_flavoure
print(f"Liquid Mix: {full_liquid_mix}")


strong_brew = ["black tea", "water"] * 3
print(f"Strong Brue: {strong_brew}")


#Bytearray
raw_spice_data = bytearray(b"CINNEMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")
