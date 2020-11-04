# Calculate the function perfomance using time taken
# Author : Kiran raj r

import time


def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


startTime = time.time()
result = calcProd()
endTime = time.time()

print(f"Time taken to complete the function {endTime - startTime}s")
