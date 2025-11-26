# You're building a ticket system for a railway app.
# Based on seat type, show its features.

# Task:
# * Input: "Sleeper", "AC", "general", "luxury"
# * Match using match-case
# * Unkown -> show: "Invalid seat type"

seat_type = input("Enter seat type (sleeper/AC/general/Luxury): ").lower()

match seat_type:
  case "sleeper":
    print("Sleeper: Basic comfort for overnight journeys.")

  case "ac":
    print("AC: Air-conditioned comfort for a pleasant journey.")

  case "general":
    print("General: Affordable seating for budget travelers.")

  case "luxury":
    print("Luxury: Premium amenities for a lavish travel experience.")

  case _:
    print("Invalid seat type")



