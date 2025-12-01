# Convert a tuple to a list, modify it, and convert back to tuple

t = (5, 20, 34, 56)

lst = list(t) # Convert to list
lst[1] = 100 # modify the tupple element

t = tuple(lst) # converting back
print(t)