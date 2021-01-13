def linearSearch (arr, elem):
    length_arr = len(arr)
    for i in range(length_arr):
        # print(arr[i])
        if arr[i] == elem:
            return "Element found"
    return "Element not found"

print(linearSearch([23,43,23,12,11,56,34,23], 11))
print(linearSearch([23,43,23,12,11,56,34,23], 119))
