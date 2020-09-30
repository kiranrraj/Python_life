newList = []
noDuplicate = []

while True:
    elem = input("Enter a letter : (type quit to quit) ")
    if elem.lower() != "quit":
        newList.append(elem)
    else:
        break

for item in newList:
    if item not in noDuplicate:
        noDuplicate.append(item)

print(noDuplicate)