print("My calculator is here")
def calculation():
    print("What do you want to do?")
    options = input("1. Addition 2. Subtraction 3. Multiplication 4. Division: ")
    if(options == "1"):
        addition()
    elif(options == "2"):
        subtraction()
    elif(options == "3"):
        multiply()
    elif(options == "4"):
        divide()
    else:
        print("Invalid input")
    print("Do you want to enter another sets of numbers?")
    choose = input("1. Yes 2. No: ")
    if(choose == "1"):
        calculation()
    else:
        print("Bye")

def addition():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    result = first_number + second_number
    print(result)

def subtraction():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    result = first_number - second_number
    print(result)
    
def multiply():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    result = first_number * second_number
    print(result)

def divide():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    result = first_number / second_number
    print(result)

calculation()