#Create an empty tuple using tuple()
print("======Tuple creation======")
tup = tuple()
print("Empty tuple created using tuple() :" ,tup)

#Create an tuple with content using tuple()
tup = tuple("kiran")
print("Empty tuple created using tuple() :" ,tup)

#Create tuple by enclosing elements 
#between parenthesie seperated by commas
myTuple = (1,2,3)
print(myTuple)

#Single element enclosed in parenthesie are treated as string 
myTupleStr = ("hello")
print("Type of ('hello')  :",type(myTupleStr))

#Single element enclosed in parenthesie must follow by 
#a comma to be treated as tuple 
myTuple = ("hello",)
print("Type of ('hello',) :",type(myTuple))

#Single element followed by a comma is also treated as tuple
#  parenthesie are optional
myTuple = "hello",
print('Type of "hello"    :',type(myTuple))

#Parenthesie are optional
myTup = "1","2","3"
print('Type of "1","2","3":',type(myTuple))
myTup= 1,2,33,4,5
print('Type of 1,2,33,4,5 :',type(myTuple))


#Accessing tuple elements (Element starts with index 0)
print("\n======Acessing tuple elements======")
myName =('k', 'i', 'r', 'a', 'n',"raj")
print(f"First element in {myName}: {myName[0]}") 
print(f"Last element in {myName}: {myName[-1]}") 
print(f"Element at 2nd position in {myName}: {myName[1]}") 
print("First letter in last element : ",myName[-1][0])
print("Last letter in last element : ",myName[-1][-1])


#Tuples are immutable but you can edit 
# mutable data type element in the tuple (eg: list)
print("\n======Tuple editing======")
try:
    myDetails[0] = "new Person"
except:
    print("Error!! Tuples are immutable")

print("\n======Tuple editing mutable data type element ======")
myTuple = (1,2,3,[4,5])
myTuple[3][0] = 10
print("(1,2,3,[4,5]) after myTuple[3][0] = 10: ",myTuple)


#Deleting a tuple, tuple elements

try:
    del myTuple[0]
except:
    print("Error cannot delete tuple elements \nTuples are immutable")

#Tuple oncatination
tupNum1 = (1,2,3)
tupNum2 = (3,4,5)
concatTup = tupNum1 + tupNum2
print("\n======Tuple concatination======")
print("Tuple one :", tupNum1)
print("Tuple two :", tupNum2)
print(f"Tuple after concatination:{tupNum1} + {tupNum2} = ", concatTup)


#Tuple Repeat
print("\n======Tuple repeat======")
print(f"{tupNum1} * 3 = {tupNum1 * 3}")


#Tuple Methods 
#Count
tupNum1 = (1,2,3,2,3,4,2,3,4,5,2,3)
print("\n======Tuple count method======")
print(f"Number of 2 in {tupNum1} is : {tupNum1.count(2)}")
print(f"Number of 3 in {tupNum1} is : {tupNum1.count(3)}")
print(f"Number of 8 in {tupNum1} is : {tupNum1.count(8)}")

