class Myself:		#Class
    country = "India"
    state = "kerala"
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

kiran = Myself("kiran", 32, 178, 82)	#Object1
arun = Myself("Arun", 34, 176, 110)	    #Object2

print(kiran.country)		#India
print(kiran.name)		    #kiran
print(kiran.age)			#32

print(arun.state)		#kerala
print(arun.height)		#176
print(arun.weight)		#110
