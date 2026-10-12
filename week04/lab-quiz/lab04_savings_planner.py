def main():
    while True:
        try:
            starting_balance = float(input("Enter starting balance: "))
            if starting_balance < 0:
                print("Starting balance cannot be negative. Please re-enter.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            monthly_deposit = float(input("Enter monthly deposit: "))
            if monthly_deposit < 0:
                print("Monthly deposit cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            interest_rate = float(input("Enter monthly interest rate (%): "))
            if interest_rate < 0:
                print("Interest rate cannot be negative. Please re-enter.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            savings_goal = float(input("Enter savings goal: "))
            if savings_goal <= 0:
                print("Savings goal must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if starting_balance >= savings_goal:
        print("The starting balance already meets or exceeds the goal.")
        return

    balance = starting_balance
    total_interest_earned = 0.0
    month = 0

    while month < 60:
        month += 1
        
        monthly_interest = balance * (interest_rate / 100)
        balance += monthly_interest
        total_interest_earned += monthly_interest
        
        balance += monthly_deposit

        print(f"Month {month}: Interest Earned = {monthly_interest:.2f}, New Balance = {balance:.2f}")

        if balance >= savings_goal:
            break

    if balance >= savings_goal:
        print(f"\nGoal reached in {month} months with a final balance of {balance:.2f} and total interest of {total_interest_earned:.2f}.")
    else:
        print(f"\nGoal not reached after 60 months with a final balance of {balance:.2f} and total interest of {total_interest_earned:.2f}.")

if __name__ == "__main__":
    main()
