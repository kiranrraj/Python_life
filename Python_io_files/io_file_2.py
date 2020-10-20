with open ('value.txt') as my_file:
    print(my_file.readlines())

with open ('new.txt', mode="w") as my_file:
     my_file.write("Message from python")