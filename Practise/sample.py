# print("""
# Menu:
#   id   product   quantity
#   101  A         24
#   102  B         100
#   103  C         239
#   104  D         231
#   105  E         129
# """)


# ids = [101, 102, 103, 104, 105]
# names = ["A", "B", "C", "D", "E"]
# qty   = [24, 100, 239, 231, 129]

# p_id = int(input("Enter product id:"))
# qnty = int(input("Enter quantity:"))
# rate = int(input("Enter product rate:"))


# index = -1
# for i in range(len(ids)):
#   if ids[i] == p_id:
#     index = i
#     break

# if index == -1:
#   print("Invalid product id!")
#   exit()


# total = rate * qnty

# print(f"\nId: {p_id}")
# print(f"Product: {names[index]}")
# print(f"Rate: {rate}")
# print(f"Quantity: {qnty}")
# print(f"Total: {total}")

# money = int(input("Give me:"))
# print(f"Change: {money - total}")




print("""
Menu:
  id   product   quantity
  101  A         24
  102  B         100
  103  C         239
  104  D         231
  105  E         129
""")


pid = int(input("Enter product id:"))
qnty = int(input("Enter quantity:"))
rate = int(input("Enter product rate:"))

if pid == 101:
  name = "A"
  stock = 24

elif pid == 102:
  name = "B"
  stock = 100

elif pid == 103:
  name = "C"
  stock = 239

elif pid == 104:
  name = "D"
  stock = 231


elif pid == 105:
  name = "E"
  stock = 129


else:
  print("Invalid product id!")


total = rate * qnty


print(f"\nId: {pid}")
print(f"Product: {name}")
print(f"Rate: {rate}")
print(f"Quantity: {qnty}")
print(f"Total: {total}")

money = int(input("Give me:"))
print(f"Change: {money - total}")

