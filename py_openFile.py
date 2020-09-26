fileName = input("Enter the file name : ")
try:
    fHandler = open(fileName)

except:
    print("Error! ")
    exit()

count= 0 
tCount = 0

for line in fHandler:
    count+=1
    if line.startswith('T'):
        tCount = tCount+1
        print("Words that starts with 'T' :",line.rstrip())

print(f'Number of lines in the file is {count}')
print(f'Number of lines in the file starting with "T" is {tCount}')