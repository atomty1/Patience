print("Welcome to Patience application")
username = input("Enter your username: ")
password = input("Enter your password: ")
print("registration successful")
print("Time to login")
login_username = input("Enter your username: ")
login_password = input("Enter your password: ")
if(username == login_username and password == login_password):
    print("Login successful")
else:
    print("Incorrect login details")
# Enter your score
# 70 - 100 : Excellent
# 60 - 69: Good
# 50 - 59: Average
# 45-49: Fair
# 40-44: Poor
# 0 - 39: Fail
# More than 100 or less than 0: Out of range
# print(type(input("Enter a number")))
# 
#  input("Enter a number")
val = input("Enter a number: ")
my_type = type(val)
print(my_type)
print(type(input("Enter a number: ")))