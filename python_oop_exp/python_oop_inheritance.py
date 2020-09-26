class Human:
    location = "earth"
    breathing = True

    def __init__(self, name, age,gender, country):
        self.name = name
        self.age = age
        self.gender = gender
        self.country = country

    def printDetails(self):
        print(f'{self.name}, {self.age}, {self.gender}, {self.country}')

vishnu = Human("Vishnu R", 25, "Male", "India")
Anitha = Human("Anitha", 52, "Female", "India")

vishnu.printDetails()
Anitha.printDetails()

class HumanKerala(Human):

    def __init__(self,name, age,gender, country,lang, state):
        Human.__init__(self, name, age,gender, country)
        self.lang = lang
        self.state = state

    def speak(self):
        print(f"I am from {self.state} and i speak {self.lang}")

    def printDetails(self):
        super().printDetails()
        print(f"From {self.state} Speaks {self.lang}")
    
vish = HumanKerala("Vishnu R", 25, "Male", "India","Malayalam", "kerala")

vish.printDetails()
vish.speak()
