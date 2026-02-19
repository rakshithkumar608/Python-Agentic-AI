class TeaLeaf:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self, value):
        if 1 <= value <= 5:
            self._age = value
        else:
            raise ValueError("Age must be between 1 and 5")


leaf = TeaLeaf(2)
print(leaf.age)   
leaf.age = 4
print(leaf.age)