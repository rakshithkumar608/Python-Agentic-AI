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

print(f"Is sugar in the order? : {'sugar' in chai_order}")

chai_order = {"type": "ginger chai", "size":"Medium", "sugar":1}
# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamon": "crushed", "ginger": "sliced"}
chai_recipi.update(extra_spices)
print(f"Updated Extra spices : {chai_recipi}")


customer_note = chai_order.get("size", "NO Note")
print(f"chai Size is :{customer_note}")