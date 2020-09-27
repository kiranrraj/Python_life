class Dog:
    """A simple oop example"""
    legs = 4
    run = True
    count = 0

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        
        Dog.count +=1
    
    def printDetails(self):
        print(f"Name : {self.name} - Age : {self.age} - Color : {self.color} - Legs = {self.legs} ")
        #if legs was Dog.legs intance cannot change the output, since here its self.legs 
        #instance can change the value of legs, which will create a entry in namespace

    def speak(self):
        print("Bow bow")


tiger = Dog("Tiger", 4, "black")
tiger.printDetails() # Name : Tiger - Age : 4 - Color : black - Legs = 4 

Dog.printDetails(tiger) # Here self get value tiger
# Name : Tiger - Age : 4 - Color : black - Legs = 4 

kaiser = Dog("Kaiser", 5, "Brown") #__init__(kaiser, "kaiser", 5, "Brown")
Dog.printDetails(kaiser) # Name : Kaiser - Age : 5 - Color : Brown - Legs = 4


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
tiger.printDetails() # Name : Tiger - Age : 4 - Color : black - Legs = 2
kaiser.printDetails() # Name : Kaiser - Age : 5 - Color : Brown - Legs = 2

tiger.legs = 3  #tiger.legs=3 create a leg attribute for tiger instance
tiger.printDetails() # Name : Tiger - Age : 4 - Color : black - Legs = 3
print(tiger.__dict__) # {'name': 'Tiger', 'age': 4, 'color': 'black', 'legs': 3} 
kaiser.printDetails() # Name : Kaiser - Age : 5 - Color : Brown - Legs = 2
print(kaiser.__dict__) # {'name': 'Kaiser', 'age': 5, 'color': 'Brown'} 

Dog.speak(tiger) # Bow bow
print(Dog.count) # 2

print(Dog.__dict__)  
#'__module__': '__main__', 
#'__doc__': 'A simple oop example',
# 'legs': 2, 
# 'run': True, 
# '__init__': <function 
# Dog.__init__ at 0x0000019B944CA310>, 
# 'printDetails': <function Dog.printDetails at 0x0000019B944CA3A0>, 
# 'speak': <function Dog.speak at 0x0000019B944CA430>, 
# '__dict__': <attribute '__dict__' of 'Dog' objects>, 
# '__weakref__': <attribute '__weakref__' of 'Dog' objects>}