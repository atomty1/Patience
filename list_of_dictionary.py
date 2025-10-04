
users = [
            {"firstname": "Taye", "lastname": "Abidakun"},
            {"firstname": "Patience", "lastname": "Pat"}

        ]



def user_func():
    main_menu = input("1. Add User 2. Display lastname of all users: ")
    if(main_menu== "1"):
        newuser_firstname = input("Enter the firstname: ")
        newuser_lastname = input("Enter the lastname: ")
        newuser = {"firstname": newuser_firstname, "lastname": newuser_lastname}
        users.append(newuser)
        print(users)
    elif(main_menu == "2"):
        for user in users:
            print(user["lastname"])
    go_back = input("Do you want to do any other thing? ")
    if(go_back == "1"):
        user_func()
    else:
        print("BYE!!!")


user_func()


