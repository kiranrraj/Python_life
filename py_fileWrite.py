fileName = input("Enter name for the file : ")

try:
    fileHandeler = open(fileName, 'w')
    while (True):
        data = input("Enter the data to be stored : ")
        if data.lower() == 'quit' : break
        fileHandeler.write(data)
except:
    print("Error occurred")
finally:
    print("Current position : ",fileHandeler.tell())
    fileHandeler.close()