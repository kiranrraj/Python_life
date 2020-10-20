# my_file = open("value.txt")
# print(my_file)
#<_io.TextIOWrapper name='value.txt' mode='r' encoding='cp1252'>

my_file = open('value.txt')

#The read method will read the whole file and the pointer will be at the
#end of the file.
print(my_file.read())
print("--------------------")
#To pust the pointer back to the start of the file use
my_file.seek(0)

print(my_file.readline())
line2 = my_file.readline().strip() #strip remove \n from the line
line3 = my_file.readline().strip()
line4 = my_file.readline().strip()
print(line2)
print(line3)
print(line4)
print("--------------------")
print(my_file.readlines())
my_file.seek(0)
print(my_file.readlines())
#['kiran raj r,\n', 'kiran nivas, \n', 'venjaramoodu,\n', 'kerala']
my_file.close()
#To close the opened file
