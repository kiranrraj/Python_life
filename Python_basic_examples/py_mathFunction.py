import math
import random

radians = 0.7
height = math.sin(radians)
print(height)

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))
print(math.sqrt(2) / 2.0)

print(random.randint(5,10))
print(random.randint(5,10))

num = [1,2,3,4,5,6,7]
print(random.choice(num))
print(random.choice(num))

for i in range(10):
    x = random.random()
    print(x)

print(math.e)
print(math.pi)
print(math.inf)
print(-math.inf)
print(math.nan)

