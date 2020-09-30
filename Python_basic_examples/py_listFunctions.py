sumList = 0
countList = 0
myList =[]

while(True):
    elem = input("Enter a number (Enter q to quit) : ")
    if elem.lower() == 'q' : break
    try:
        myList.append(int(elem))
        countList+=1
        sumList+=int(elem)
    except:
        print("Error occurred!!!!")
        quit()
    
avg = sumList / countList
print("Length of the list is        : ", countList)
print("Average value of the list is : ", avg)
print("Highest value in the list is : ", max(myList))
print("Lowest value in the list is  : ", min(myList))
