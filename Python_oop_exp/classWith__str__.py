class Person:
    location = "earth"
    species = "human"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak (self,lang):
        print(f"I speak {lang.capitalize()}")
    
    def __str__(self):
        return (f"Details: {self.name.capitalize()}, {self.age}, {self.gender.capitalize()}")

k1 = Person('kira', 32, "male")

print(k1)
