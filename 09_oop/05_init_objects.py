class OrderChai:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml {self.type} chai ordered."

order = OrderChai("Masala", 200)
print(order.summary())

order_two = OrderChai("Ginger", 150)
print(order_two.summary())

order_three = OrderChai("Cardamom", 250)
print(order_three.summary())