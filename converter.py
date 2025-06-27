print("Welcome")
def convert():
    celc = float(input("Enter the celcius you want to convert: "))
    result = 273.15 + celc
    print(result)
    continue_task()

def continue_task():
    print("Do you want to continue: ")
    option = input("Y for Yes,  N for NO: ")
    if(option == "Y"):
        convert()
    else:
        print("Bye")

convert()