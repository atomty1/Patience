val = []
def add_user():
    person1 = {"name": "Taye", "dept": "CSC", "age": 10}
    person2 = {"name": "Peter", "dept": "PSG", "age": 20}
    person3 = {"name": "John", "dept": "BCH", "age": 30}
    person4 = {"name": "Andrew", "dept": "CHM", "age": 5}
    val.append(person1)
    val.append(person2)
    val.append(person3)
    val.append(person4)


# names = ("Patience", "Adorable", "Anabel")
def display_oldest():
    highest = 0
    for n in val:
        abc = n["age"]
        if (abc > highest):
            highest = abc
    print(highest)







