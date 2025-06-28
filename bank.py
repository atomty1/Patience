balance = 0
def bank():
    print("Welcome to my bank app.")
    main_menu = input("1. Deposit 2. Withdraw: ")
    if(main_menu == "1"):
        deposit_func()
    elif(main_menu == "2"):
        withdraw_func()
    print("Do you want to perform another transaction?")
    choice = input("1. Yes 2. No: ")
    if(choice == "1"):
        bank()
    else:
        print("Bye. Thanks for banking with us.")

def deposit_func():
    global balance
    deposit_value = float(input("Enter the amount you want to deposit: "))
    balance = deposit_value
    print(f"Your balance is {balance}")

def withdraw_func():
    global balance
    withdraw_value = float(input("Enter the amount you want to withdraw: "))
    balance = balance - withdraw_value
    print(f"Your balance is {balance}")

bank()