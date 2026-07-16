#Banking Program

def check_balance():
    print(f"Your balance is: {balance:.2f}")

def deposit():
    amount = float(input("Enter amount: "))
    if amount < 0:
        print("Error❌")
        print("Your deposit cannot be negeative!")
        return 0
    else:
        return amount

def withdraw():
    pass


balance = 0
running = True

while running:
    print("1. Check Balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("Please Enter your choice?(1-4): "))

    if choice == 1:
        check_balance()
    elif choice == 2:
        amount+=deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        running = False
    else:
        print("Please Enter only a valid number!")

     