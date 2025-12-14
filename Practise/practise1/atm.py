user = {
    "name": "Rakshith",
    "pin": "1234",
    "balance": 5000
}

attempts = 3

#  PIN VALIDATION 
while attempts > 0:
    pin = input("Enter your ATM PIN: ")

    if len(pin) == 4 and pin.isdigit():
        if pin == user["pin"]:
            print("Login successful")
            break
        else:
            attempts -= 1
            print(f"Wrong PIN. Attempts left: {attempts}")
    else:
        attempts -= 1
        print(f"Invalid PIN format. Attempts left: {attempts}")

else:
    print("ATM blocked. Too many wrong attempts.")
    exit()

#  ATM MENU 
while True:
    print("\n1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your balance is {user['balance']}")

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= user["balance"]:
            user["balance"] -= amount
            print(f"Collect cash. Balance: {user['balance']}")
        else:
            print("Insufficient balance")

    elif choice == "3":
        amount = int(input("Enter amount to deposit: "))
        user["balance"] += amount
        print(f"Amount deposited. Balance: {user['balance']}")

    elif choice == "4":
        old_pin = input("Enter old PIN: ")
        if old_pin == user["pin"]:
            new_pin = input("Enter 4-digit new PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                user["pin"] = new_pin
                print("PIN changed successfully")
            else:
                print("Invalid PIN format")
        else:
            print("Old PIN is incorrect")

    elif choice == "5":
        print("Thank you. Visit again.")
        break

    else:
        print("Invalid option")
