all_persons = []
def handle_persons():
    print("What would you like to do?")
    menu = input("1. Add person 2. Get oldest person: ")
    if(menu == "1"):
        add_person()
    elif( menu == "2"):
        get_oldest()
    
    print("Do ypu wan to anything else?")
    repeat = input("1. Yes 2. No: ")
    if repeat == "1":
        handle_persons()
    else:
        print("BYE!!!")


def add_person():
    fName = input("Enter firstname: ") #Peter
    department = input("Enter the department: ") # CSC
    person_age = int(input("Enter the age: ")) #20
    new_person = {"firstname": fName, "dept": department, "age": person_age}
    all_persons.append(new_person)
    print(f"{fName} has been added successfully.")
    print(all_persons)
   


def get_oldest():
    highest_age = all_persons[0]["age"]
    oldest_person = all_persons[0]
    for person in all_persons:
        if person["age"] > highest_age:
            highest_age = person["age"]
            oldest_person = person
    print(f"The olderst person is {oldest_person["firstname"]}, who is {highest_age} years old")



    

handle_persons()


# nums = [8, 10, 20]
# result = 0
# for n in nums:
#     result = result + n
# print(result)
