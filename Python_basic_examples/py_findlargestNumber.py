num = int(input("Enter a number, zero to exit "))

#Creating a list 
newList = [num]
largest = num

while num != 0:
    num = int(input("Enter a number, zero to exit "))
    #appending a new item to the list
    newList.append(num)
    print(newList)

if len(newList) == 1:
    print("The largest number is : " + str(newList[0]))
elif len(newList) > 1:
    for item in newList:
        if item > largest:
            largest = item
    print("The largest item is : "+ str(largest))
else:
    print("Some error occured ")
    