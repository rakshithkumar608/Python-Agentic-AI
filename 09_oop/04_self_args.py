class Chaicup:
    size = 150

    def describe(self):
        return f"This is a {self.size}ml cup of chai."

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))


cup_two = Chaicup()
cup_two.size = 200
print(Chaicup.describe(cup_two))