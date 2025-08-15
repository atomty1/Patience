names = []
["Peter", "James", "John"]
def my_func():
    menu = input("1. Add 2. Remove 3. Edit: ")
    if(menu == "3"):
        print(names)
        new_name = input("Enter the new name: ")
        index = int(input("Enter the index you want to change: "))
        names[index] = new_name
        print(f"{new_name} added successfully.")

