# Object Oriented Programming - OOP
class Human:
    eyes = 2
    ears = 2
    head = 1
    def eat(self):
        print("I am eating")
    
    def sleep(self, duration, side):
        print(f"I got {self.eyes} eyes")
        # print(f"I am having a good time sleeping and rolling to the {side}  for {duration} hours")
adam = Human()
eve = Human()
adam.eyes = 1
# print(adam.eyes)
# print(eve.eyes)
adam.sleep(8, "left")
eve.sleep(6, "right")
# print(adam.eyes)
# print(adam.head)
# print(eve.eyes)