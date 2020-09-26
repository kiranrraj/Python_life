class Dog:
    legs = 4
    run = True

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def printDetails(self):
        print(f"Name : {self.name} - Age : {self.age} - Color : {self.color} - Legs = {Dog.legs} ")

    def speak(self):
        print("Bow bow")

tiger = Dog("Tiger", 4, "black")
tiger.printDetails()
# Name : Tiger - Age : 4 - Color : black - Legs = 4 

Dog.printDetails(tiger) # Here self get value tiger
# Name : Tiger - Age : 4 - Color : black - Legs = 4 

kaiser = Dog("Kaiser", 5, "Brown") #__init__(kaiser, "kaiser", 5, "Brown")
Dog.printDetails(kaiser)
# Name : Kaiser - Age : 5 - Color : Brown - Legs = 4

#SAME LOCATION FOR CLASS VARIABLE
# print(id(tiger.legs))   #140725336479488
# print(id(kaiser.legs))  #140725336479488
# print(id(Dog.legs))     #140725336479488

# Dog.legs = 2

# print(id(tiger.legs))   #140725336479424
# print(id(kaiser.legs))  #140725336479424
# print(id(Dog.legs))     #140725336479424

# print(id(kaiser.name))  #2781624086192
# print(id(tiger.name))   #2781624086000

Dog.legs = 2

tiger.printDetails()
kaiser.printDetails()
# Name : Tiger - Age : 4 - Color : black - Legs = 2
# Name : Kaiser - Age : 5 - Color : Brown - Legs = 2

Dog.speak(tiger)
#Bow bow