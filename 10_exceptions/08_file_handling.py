# file = open("order.txt", "w")
# try:
#     file.write("Masala Chai - 2 cups")
# finally:
#     file.close()


with open("orders.txt", "w") as file:
    file.write("Masala Chai - 4 cups")