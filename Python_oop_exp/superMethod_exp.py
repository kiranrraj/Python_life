#Author : Kiran Raj R
#Date   : 5/10/2020
#Topic  : super()

class Person:

    """A class that used super() method"""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def printDetails(self):
        print(f"Details: {self.name.capitalize()}, {self.age}, {self.gender.capitalize()}")

class Indian(Person):

    nationality = 'Indian'

    def __init__(self, name, age, gender,state):
        super().__init__(name, age, gender)
        #super help to aceess base class method
        self.state = state

    def printDetails(self):
        super().printDetails()
        print(f"Nationality: {self.nationality}\nState: {self.state}")

class Keralite(Person):

    def __init__(self, name, age, gender, state='Kerala'):
        super().__init__(name, age, gender)
        self.state = state

    def printDetails(self):
        super().printDetails()
        print(f"Nationality: {Indian.nationality}\nState: {self.state}")
        print("Official language: Malayalam")

class Trivian(Keralite):

    def __init__(self, name, age, gender, district, state="Kerala"):
        Keralite.__init__(self,name, age, gender, state)
        self.district = district

    def printDetails(self):
        Keralite.printDetails(self)
        print(f"District: {self.district}")


k1 = Indian('kira', 32, 'male', 'kerala')
k1.printDetails()
print("----------------------------------")
k2 = Keralite('viru', 38, 'male')
k2.printDetails()
print("----------------------------------")
k3 = Trivian('kira', 32, 'male','Trivandrum')
k3.printDetails()