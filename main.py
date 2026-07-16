#Banking Program

def check_balance(balance):
    print("-" * 30)
    print(f"Your balance is: ${balance:.2f}")
    print("-" * 30)
def deposit():
    amount = float(input("Enter amount: "))
    if amount < 0:
        print("-" * 30)
        print("Error❌")
        print("Your deposit cannot be negeative!")
        print("-" * 30)
        return 0
    else:
        return amount

def withdraw(balance):
    money = float(input("Enter amount: "))
    if money > balance:
        print("Insufficient funds!")
        return 0
    elif money < 0:
        print("amount cant be negative.")
        return 0
    else:
        return money
    
def main():
    balance = 0
    running = True
    while running:
        print("*" * 30)
        print("KIDUS BANK🏦")
        print("*" * 30)
        print("1. Check Balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")

        choice = int(input("Please Enter your choice?(1-4): "))

        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            balance+=deposit()
            print("Deposit Successful!✅")
        elif choice == 3:
            balance-=withdraw(balance)
            print("-" * 30)
            print("Withdrawn sucessful!✅")
            print("-" * 30)
        elif choice == 4:
            running = False
        else:
          print("Please Enter only a valid number!")
if __name__ == "__main__":            
    main()
print("-" * 30)
print("Thank you for working with us!🌼")
print("-" * 30)