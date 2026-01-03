
fav_chais = [
  "Masala Chai", "Green Tea", "Masala Chai", "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in fav_chais}
print(unique_chai)


recipes = {
  "Masala Chai" : ["ginger", "cardamom", "cloves"],
  "Elaichi Chai" : ["cardamom", "milk"],
  "Spicy Chai" : ["ginger", "black pepper", "cloves"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)