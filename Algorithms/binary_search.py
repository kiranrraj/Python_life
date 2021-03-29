def binarySearch(myList, search_item):
    first = 0
    last = len(myList) - 1
    flag = False

    while first <= last: 
        mid = (first + last)//2
        if myList[mid] == search_item:	            
            return f"Item found at position {mid +1}"     
        else:
            if search_item < myList[mid]:
                last = mid-1
            else:
                first = mid+1

    return"Not Found!!!"

print(binarySearch([1,2,3,4,5,6,7,8,9,10], 3))
print(binarySearch([1,2,3,4,5,6,7,8,9,10], 9))
print(binarySearch([1,2,3,4,5,6,7,8,9,10], 7))
print(binarySearch([1,2,3,4,5,6,7,7,7,7,7,8,9,10], 7))
print(binarySearch([1,2,3,4,5,6], 4))
print(binarySearch([1,2,3,4,5,6], 0))
