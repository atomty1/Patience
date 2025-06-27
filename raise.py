print("Welcome")
def bmi():
    a = input("Enter your weight: ")
    b = input("Enter your height: ")
    result = a / b ** 2
    if result < 18.5:
        print("Underweight")
    elif result >= 18.5 and result <= 24.0:
        print("Normal")
    elif result > 24:
        print("Obese")
