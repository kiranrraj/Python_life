#creating a list
myName_list = ['k','i','r','a','n',"r","a","j"]

#printing a list using for loop
for item in myName_list:
    print(item, end=" ")
print()

print(myName_list[:5]) #print elements from 0 to 4
print(myName_list[:-3]) #print elements from -4 t0 end

print(myName_list[5:]) #print elements from 5 to end
print(myName_list[-3:]) #prints elements from -3 t0 -1

print(myName_list[:]) #print entire list elements
print("Length of list : ",len(myName_list)) #prints length of the list

#return the index of the specified element(First occurance)
print("Index of first 'r' in the list : ",myName_list.index('r'))

#Return the number of occurance of the specified element
print("Number of 'r' in the list : ",myName_list.count('r'))
print("Number of 'a' in the list : ",myName_list.count('a'))

#adding elements into list (append add elements at the end)
myName_list.append(".")
myName_list.append("R")
print("List after appending : ",myName_list)

#editing element in the specified position
myName_list[0] = "K"
print("List after editing : ", myName_list)

#check whether a element in a list
print("a" in myName_list)
print("z" in myName_list)

#concatinating lists
fName = ["k","i","r",]
lName = ["a","n"]
fullName = fName + lName
print("Concat two list",fName, " and ",lName, " = ", fullName)

#insert element at position specified
myName_list.insert(5,"__")
print("List after inserting underscore : ",myName_list)

#deleting an item from specified position
del myName_list[5]
print("List after deleting underscore : ",myName_list)

#delete multiple elements
del myName_list[5:]
print("List after removing elements from index 5 :",myName_list)

#delete an entire list
del fullName

#remove the specified element
myName_list.remove('r')
print("List after removing 'r' : ",myName_list)

#pop an element
myName_list.pop()
print("List after pop operation : ",myName_list)

myName_list.pop(0)
print("List after pop operation at index 0 : ",myName_list)

#extending from another list
fName = ["k","i","r"]
lName = ["a","n"]
fName.extend(lName)
print("List after extending a list : ", fName)

num= ["a","b","c"]
fName[len(fName):] = num
print("List after extending one more list : ", fName)

#sort the elements
fName.sort()
print("List after sorted", fName)

#reverse sort the list
fName.reverse()
print("List after reverse sorted", fName)

fName.sort()

#reverse the list using sort method with reverse key set
fName.sort(reverse=True)
print("List after reverse sorted using sort()", fName)

#Listed copied
newList = fName.copy()
print("Listed copied using copy()", newList)

#Remove all elements from a list
fName.clear()
print("After using clear method : ", fName)

numbers = [1,2,3,4,5,6,7,8,9,10]
print("Length of the number list is : ", len(numbers))
print("Sum of the elements in the list is : ", sum(numbers))
print("Highest value in the list is : ", max(numbers))
print("Lowest value in the list is : ", min(numbers))
print("Average value of the list is : ", sum(numbers) / len(numbers))