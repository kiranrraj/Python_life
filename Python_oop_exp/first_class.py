class MyfirstClass:
    pass

# --------------------------------------- #

class Point:
    pass

obj1 = Point()
obj2 = Point()

obj1.x = 5
obj1.y = 10

obj2.x = 100
obj2.y = 110

# print(obj1.x, obj1.y)
# print(obj2.x, obj2.y)

# --------------------------------------- #

class Point1:
    """Simple class"""

    def reset(self):
        self.x = 0
        self.y = 0

obj3 = Point1()

obj3.x = 1000
obj3.y = 2000
print(obj3.x, obj3.y)
obj3.reset()

print("Value after the reset call")
print(obj3.x, obj3.y)

obj3.x = 1000
obj3.y = 2000
print(obj3.x, obj3.y)

# #TypeError: reset() missing 1 required positional argument: 'self'
# Point1.reset()  

Point1.reset(obj3)
print("Value after the reset call - 2")
print(obj3.x, obj3.y)