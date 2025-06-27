print("welome")
def grade_student():
    score = float(input("Enter your score: "))
    if(score > 100 or score < 0):
        print("Out of range")
    elif(score >= 70):
        print("Excellent")
    elif(score >= 60):
        print("Good")
    elif(score >= 50):
        print("Average")
    elif(score >= 45):
        print("Fair")
    elif(score >= 40):
        print("Poor")
    elif(score >= 0):
        print("Fail")
    repeat_task()

def repeat_task():
    print("Do you want to continue?")
    a = input("1. Yes 2. No: ") 
    if(a == "1"):
        grade_student()
    else:
        print("Bye")


grade_student()
