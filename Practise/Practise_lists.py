car_brands = ["BMW", "Mercedes", "Bugati", "Lambo"]
print(f"The Most Popular Cars : {car_brands}")


#Accessing list elements
print(f"The first element of the List is: {car_brands[0]}")
print(f"The element of the List is: {car_brands[1:3]}")
print(f"The first two element of the List is: {car_brands[:2]}")
print(f"The last two element of the List is: {car_brands[-2]}")

#changing the elements on list
car_brands[2] = "Bentley"
print(f"After Changing the element in list is: {car_brands}")

#Inserting the new element in the list
car_brands.insert(3,"Aston martin")
print(f"After inserting to the list:{car_brands}")


#Adding element(append)
car_brands.append("Rolls Royce")
print(f"After Adding element to the list : {car_brands}")

#Extending the both list
car_brands = ["BMW", "Mercedes", "Bugati", "Lambo"]
car_specifications = ["fully charged", "Turbo", "Petrol", "Disel"]
car_brands.extend(car_specifications)
print(f"After Extending the list : {car_brands}")

#Removing the element
car_brands.remove("Bugati")
print(f"After removing the element from the list:{car_brands}")

#pop (removes element at specific position) last added element
car_brands.pop()
print(f"After pop: {car_brands}")

#removing the elements
car_brands.remove("Lambo")
print(f"After removing : {car_brands}")

#clear and Delete it clears all full list
car_brands.clear()

print(f"Clearing list : {car_brands}")



