num = []
inNum = int(input("Enter the number (press 0 to quit) "))

while True:
    inNum = int(input("Enter the number (press 0 to quit) "))
    if inNum == 0:
        break
    else:
        num.append(inNum)

 
largest = 0
smallest = num[0]

for item in num:
    if(largest < item):
        largest = item

    if(smallest > item ):
        smallest = item

print("The smallest number is : ", smallest)
print("The largest number is : ", largest)
