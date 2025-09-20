# vals = [9, 30, 50, 70, 4, 50]
# vals.remove(50)
# vals.remove(50)
# # vals.pop(2)
# print(vals)
# print(f"The name of my school is {schools[0]}")
# print(f"The name of my school is {schools[1]}")
# print(f"The name of my school is {schools[2]}")

# schools.append("OAU")
# schools.append("MIT")
# print(schools)
# print(abc)
# print(False)
# school = ["OAU", "UI", "LAUTECH"]
# for i in school:
#     print(f"I attend {i}")



names = []
print("Welcome here.")
def names_func():
    option = input("1. To add a new name. 2. To display all names: ")
    if(option == "1"):
        add_name = input("Enter your name: ")
        names.append(add_name)
        print(f"{add_name} added successfully.")
    elif(option == "2"):
        for val in names:
            print(f"My name is {val}")
    
    print("Do you want to do anything else?")
    choice = int(input("1. Yes 2. No: "))
    if(choice == 1):
        names_func()
    else:
        print("Byeee!")
    
    
    

names_func()

# ["Hello world", "How are you doing today?"]
# 1. Add a new post  2. To display all posts 3. To delete a post
# 1. Enter your post.
#     Post added successfully
# 2. Display all posts

# 3. Enter the index of the post that you want to delete
#     Post removed successfully.

# Do you want to do anything else? 1. Yes 2. No.

# vals = [10, 20, 30]

# for a in vals:
#     print("Hello")
#     print("a")
#     print("Hi")
#     print(a)

names = ["Happy", "Patience", "John"]
for display_name in names:
    print(f"Good morning {display_name}")