class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 30, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not availabel")

        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")

        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Thank you for visiting our chai shop!")

bill("ginger", 2)
bill("masala", "three")
bill("mint", 3)
