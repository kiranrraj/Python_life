name = "kiran raj r"
fullname = "KIRAN"
print(name[0])
print(len(name))

for char in name:
    print(char, end=" ")
print()


index = 0
while index <len(name):
    print(name[index], end="*")
    index = index + 1
print()

print(name, " convert into upper case : ",name.upper())
print(name, " after capitalization : ",name.capitalize())
print(fullname, " Convert into lower case : ",fullname.lower())

index = name.find('a')
print("Index of first 'a' : ",index)

index = name.find('a', 5)
print("Index of first 'a' after index 5 : ",index)

for i in range(25,0,-1):
    print(i)
print(type(name))
