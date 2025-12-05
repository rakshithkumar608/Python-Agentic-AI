# A store tracks customers and their reward points.
# Each customer has a purchase amount and a reward code that gives either percentage-based points or fixed points.

# customers = [
#   {"id": 101, "amount": 250, "reward": "R10"},
#   {"id": 102, "amount": 400, "reward": "B50"},
#   {"id": 103, "amount": 120, "reward": "R20"}
# ]

# rewards = {
#   "R10": (0.10, 0),   # 10% reward
#   "B50": (0, 50),     # fixed 50 points
#   "R20": (0.20, 0)    # 20% reward
# }

# # Task:
# # For each customer, calculate reward points
# # Points = amount * percent + fixed
# # Print: "<id> earned <points> reward points"

customers = [
  {"id": 101, "amount": 250, "reward": "R10"},
  {"id": 102, "amount": 400, "reward": "B50"},
  {"id": 103, "amount": 120, "reward": "R20"}
]

rewards = {
  "R10": (0.10, 0),   # 10% reward
  "B50": (0, 50),     # fixed 50 points
  "R20": (0.20, 0)    # 20% reward
}


for customer in customers:
    percent, fixed = rewards.get(customer["reward"], (0, 0))
    points = customer["amount"] * percent + fixed
    print(f"{customer['id']} earned {points} reward points")

