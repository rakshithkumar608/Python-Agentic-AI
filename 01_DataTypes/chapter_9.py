#Sets

essential_spices = {"cardamon", "ginger", "cinamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

#union
all_spices = essential_spices | optional_spices
print(f"All Spices : {all_spices}")

#intersection
common_spices = essential_spices & optional_spices
print(f"common Spices : {common_spices}")

#only shows the values of the essential_spices
only_in_essential = essential_spices - optional_spices
print(f"Only in essential  Spices : {only_in_essential}")

print(f"Is 'cloves' in optional spices? :{'cloves' in optional_spices}")


