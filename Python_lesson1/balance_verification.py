def verify_balance():
    balance = 1000

    print("Welcome to the ATM")
    while balance >= 0:
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount == 0:
                print("Leaving ATM")
                break
            elif amount > balance:
                 print(f"Insufficient funds. Your balance is ${balance:.3f}.")
            elif amount < 0:
                print("Invalid amount")
            else:
                balance-= amount
                print(f"Withdrawal successful! Your new balance is ${balance:.3f}.")

        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    if balance == 0:
        print("No txns allowed")

verify_balance()



