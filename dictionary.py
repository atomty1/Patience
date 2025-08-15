students = [
                {"name": "John", "dept": "Physiology"},
                {"name": "Patience", "dept": "Medicine"},
                {"name": "Chinanza", "dept": "Nursing"},
         

            ]


def school():
    print("Welcome to my school.")
    print("What do you want to do?")
    main_menu = input("1. Add student 2. Edit student info 3. Show all names 4. Remove a student: ")
    if(main_menu == "1"):
        add_student()
    elif(main_menu == "2"):
        edit_student()
    elif(main_menu == "3"):
        show_names()
    elif(main_menu == "4"):
        remove_student()
    
    print("Do you want to perform another operation?")
    go_back = input("y. Yes n. No: ")
    if(go_back == 'y'):
        school()
    else:
        print("Bye.")
    
def add_student():
    student_name = input("Enter the name of the student: ")
    student_dept = input("Enter the department of the student: ")
    new_student = {"name": student_name, "dept": student_dept}
    students.append(new_student)
    print(f"{student_name} added sucessfully.")
    print(students)

def edit_student():
    index = int(input("Enter index of the student you want to edit: "))
    key = input("Enter the key you want to edit: ")
    value = input("Enter the value for that key: ")
    students[index][key] = value
    print(f"{key} changed successfully.")
    print(students)


def show_names():
    for student in students:
        print(student["name"])  

def remove_student():
    index = int(input("Enter the index of the student you want to remove: "))
    del students[index]
    print(students)


    



school()

# val = {"school": "UI", "dept": "ANB", "name": "Esther"}
# key = input("Enter the key you want to change: ")
# value = input("Enter the value: ")
# val[key] = value
# print(val)
# school_name = input("Enter the school name: ")
# dept_name = input("Enter the department: ")
# student_name = input("Enter your name: ")
# val["school"] = school_name
# val["dept"] = dept_name
# val["name"] = student_name
# print(val)