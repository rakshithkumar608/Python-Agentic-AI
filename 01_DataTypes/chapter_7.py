masala_spices = ("cardamon", "cloves", "cinnamon")

(spices1, spices2, spices3) = masala_spices
print(f"Main masala spices : {spices1}, {spices2}, {spices3}")

ginger_ratio, cadramon_ratio = 2, 1
print(f"Ratio is G : {ginger_ratio} and C :{cadramon_ratio}")
ginger_ratio, cadramon_ratio = cadramon_ratio, ginger_ratio
print(f"Ratio is G : {ginger_ratio} and C :{cadramon_ratio}")


#membership testing

print(f"Is ginger in masala spices ? {'ginger' in masala_spices}")
print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")
