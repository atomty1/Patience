# names = ["Peter", "James", "John"]
# for name in names:
#     print(f"My name is {name}")

names = [
            {"name": "Peter", "location": "Nigeria", "age": 20},
            {"name": "John", "location": "UK", "age": 30},
            {"name": "Andrew", "location": "Ghana", "age": 40},

        ]

for anything in names:
    print(f"My name is {anything["name"]}, I live in {anything["location"]}")