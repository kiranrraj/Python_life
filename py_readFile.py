fileName = input("Enter the file name : ")
try:
    fileHandler = open(fileName)
except: 
    print("Some error occurred")

data = fileHandler.read()
print("File Contents : ")
print(data)