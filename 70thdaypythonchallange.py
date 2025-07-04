# Python Banking Program


def show_balance(balance):
    print(f" Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount you want to deposit: ? "))

    if amount < 0:
        print("This is not a valid amount.")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("Enter the amount you want to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero.")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("****************")
        print("Banking program")
        print("****************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice(1-4): "))
        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print("This is not a valid choice")

    print("Thank you have a nice day ahead !")

if __name__ == "__main__":
    main()
