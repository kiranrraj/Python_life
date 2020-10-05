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


print("-----------------------------------")
vishnu = Person("vishnu", 25, "male")
vishnu.printDetails()   # Details: Vishnu, 25, Male
vishnu.speak("malayalam")   # I speak malayalam 
print(vishnu.__class__.location) # earth      Access class attribute
print(Person.location)  # earth
print(vishnu.location)  # earth
print(vishnu.name)      # vishnu
print("-----------------------------------")
kiran = Person("kiran", 32, "male")
kiran.printDetails()        # Details: Kiran, 32, Male
kiran.speak("malayalam")    # I speak malayalam 
print(kiran.location)       # earth
print(kiran.species)        # human
print("-----------------------------------")
kiran.fullname = "kiran raj r"
print(kiran.fullname)   #kiran raj r
# print(vishnu.fullname)  AttributeError: 'Person' object has no attribute 'fullname'
Person.line = " -----"
print(kiran.line)   # -----
print(vishnu.line)  # -----






