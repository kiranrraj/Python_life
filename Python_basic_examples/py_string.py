msg = "Hello World"
print(msg[0]) #index starts with 0
print(msg[4]) #prints fifth letter
print(msg[-1]) #prints last letter
print(msg[-5]) #prints 5th letter from last

print(msg[0:5])  # index 5 is excluded
print(msg[6:]) #prints letters from position 6 to end
print(msg[:])   #prints all letters

msgf = f'{msg}, again'  #formated 
print(msgf)

print(len(msgf))
print(msg.upper())  # to uppercase
print(msg.lower())  # to lower case

print(msg.find('W'))
print(msg.find("orld"))
print(msg.replace('Hello', 'H3ll0'))
print(msg)
print("Hello" in msg)
print("hello" in msg)
name = "kiran raj r"
print(name.title())