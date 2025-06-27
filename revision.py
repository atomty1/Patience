def display_vote():
    age = int(input("Enter your age: "))
    name = input("Enter your name: ")
    if age > 18:
        print(f"{name} You can vote")
    elif age > 13:
        print(f"{name} You are a teen")
    else:
        print(f"{name} You are too young to be here")
    run_again()
    
    
def run_again():
    print("Do you want to go again?")
    choice = input("Y. Yes N. No: ")
    if(choice == "Y"):
        display_vote()
    else:
        print("good bye.")

display_vote()