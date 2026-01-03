deposit = int(input("Enter the amount to deposit: "))
print("Initial balance:", deposit)

while deposit >= 1000:
    withdraw = int(input("Enter the amount to withdraw: "))

    if deposit - withdraw >= 1000:
        deposit = deposit - withdraw
        print("Withdrawal successful")
        print("Remaining balance:", deposit)
    else:
        print("Minimum balance should be maintained: 1000")
        break
