import array

# array(dataType, valueList)
arr = array.array('i',[1,2,3,4,5])

print("Array elements : ", end=" ")
for i in range(0,len(arr)):
    print(arr[i], end= " ")
print("\r")


# append an element at the end of the array
#arrayName.append(element)
arr.append(6)

print("Array elements after append operation : ", end=" ")
for i in range(0,len(arr)):
    print(arr[i], end= " ")
print("\r")


# insert an element at a position specified
# arrayName.insert(position, element)
arr.insert(0,0)

print("Array elements after insertion : ", end=" ")
for i in range(0,len(arr)):
    print(arr[i], end= " ")
print("\r")


#remove the last element
#arrayName.pop()
elem = arr.pop()

#print the popped element
print("Element pop using pop opeartion : " + str(elem)) 

print("Array elements after pop operation : ", end=" ")
for i in range(0,len(arr)):
    print(arr[i], end= " ")
print("\r")


# remove the element specified by position
# arrayName(position)
elem = arr.pop(2)

#print the popped element
print("Element pop using pop opeartion(position) : " + str(elem)) 

print("Array elements after pop operation using position : ", end=" ")
for i in range(0,len(arr)):
    print(arr[i], end= " ")
print("\r")


# remove an element specified
arr.remove(0)

print("Array elements after remove operation : ", end=" ")
for i in range(0,len(arr)):
    print(arr[i], end= " ")
print("\r")