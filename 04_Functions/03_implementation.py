# Hiding Implementation Details

# You'r building a simple app that register users.
# You want to seperate concerns: getting input, validating it, and saving it.

# Task:
#  * Write register_user() that calls:
#      * get_input()
#      * validate_input()
#      * save_to_db()

def get_input():
  print("Getting user input")

def validate_input():
  print("Validating the user information")

def save_to_db():
  print("saving to database")


def register_user():
  get_input()
  validate_input()
  save_to_db()
  print("Register saved")

register_user()