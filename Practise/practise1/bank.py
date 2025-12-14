users = {
    "1001": {"name": "Rakshith", "pin": "1234", "balance": 5000},
    "1002": {"name": "Ravi", "pin": "4321", "balance": 3000},
    "1003": {"name": "Asha", "pin": "1111", "balance": 7000}
}

acc_no = input("Enter account number: ")

if acc_no in users:
    pin = input("Enter PIN: ")

    if pin == users[acc_no]["pin"]:
        print("Login successful")

        current_user = users[acc_no]

        while True:
            print("\n1. Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")

            choice = input("Choose: ")

            if choice == "1":
                print("Balance:", current_user["balance"])

            elif choice == "2":
                amt = int(input("Enter amount: "))
                if amt <= current_user["balance"]:
                    current_user["balance"] -= amt
                    print("Withdrawn. Balance:", current_user["balance"])
                else:
                    print("Insufficient funds")

            elif choice == "3":
                amt = int(input("Enter amount: "))
                current_user["balance"] += amt
                print("Deposited. Balance:", current_user["balance"])

            elif choice == "4":
                print("Logged out")
                break
            else:
                print("Invalid option")
    else:
        print("Wrong PIN")
else:
    print("Account not found")
