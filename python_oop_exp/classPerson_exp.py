class Person:
    location = "earth"
    species = "human"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak (self,lang):
        print(f"I speak {lang.capitalize()}")
    
    def printDetails(self):
        print(f"Details: {self.name.capitalize()}, {self.age}, {self.gender.capitalize()}")


vishnu = Person("vishnu", 25, "male")
vishnu.printDetails()
vishnu.speak("malayalam")
print(vishnu.__class__.location) #Access class attribute
print(vishnu.location)
print(vishnu.name) 

