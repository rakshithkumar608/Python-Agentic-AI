#Dictinory

chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")


chai_recipi = {}
chai_recipi["base"] = "black tea"
chai_recipi["liquid"] = "milk"

print(f"Recipe Base: {chai_recipi["base"]}")
print(f"Recipe Liquid: {chai_recipi["liquid"]}")
print(f"Recipe: {chai_recipi}")

del chai_recipi["liquid"]
print(f"Recipe: {chai_recipi}")