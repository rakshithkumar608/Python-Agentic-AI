class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)


# creating objects from class chai

masala = Chai()
print(f"Masala chai is from: {masala.origin}")
print(f"Masala chai is hot: {masala.is_hot}")
masala.is_hot = False
print("Class:", Chai.is_hot)
print(f"Masala chai is hot: {masala.is_hot}")

masala.flavor = "Masala"
print(f"The flavour: {masala.flavor}")


# Example program

class Car:
    car = "BMW"
    model = "M5"
    year = "2023"
    place = "Germany"

print(f"The car is: {Car.car}")
print(f"The Car model: {Car.model}")
print(f"The Car year: {Car.year}")
print(f"The Car place: {Car.place}")


class Model:
    model = "M3"

print(f"The Old Car model: {Car.model}")
print(f"The new Car Model: {Model.model}")

Model.year = "2022"
print(f"The model year of an car:{Model.year}")