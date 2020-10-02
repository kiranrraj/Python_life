# This program find the kth smallest number in the array
# Assuming that k is less than length of array and array has no duplicate elements

def find_k(arr, modifier, k):
    arr = sorted(arr);
    modifier = modifier.lower().strip()
    length = len(arr)
    if length < k: 
        print(f"The value of k should be less than or equal to the length of array.\nUser input \nk : {k}\nArray Length: {length} ")
    else:
        if modifier == 'smallest':
            print(f"The k-th smallest element in the array {arr} where k is {k} => {arr[k-1]}")
        elif modifier == 'largest':
            print(f"The k-th largest element in the array {arr} where k is {k} => {arr[length-k]}")


num = [3, 5, 7, 9, 100, 11, 45, 32, 1]



print("-----------------------")
find_k(num, 'smallest', 3)
# The k-th smallest element in the array [1, 3, 5, 7, 9, 11, 32, 45, 100] where k is 3 => 5

find_k(num, 'largest', 3)
# The k-th largest element in the array [1, 3, 5, 7, 9, 11, 32, 45, 100] where k is 3 => 32

find_k(num, 'smallest', 9)
# The k-th smallest element in the array [1, 3, 5, 7, 9, 11, 32, 45, 100] where k is 9 => 100

find_k(num, 'largest', 9)
# The k-th largest element in the array [1, 3, 5, 7, 9, 11, 32, 45, 100] where k is 9 => 1

find_k(num, 'largest', 10)
# The value of k should be less than or equal to the length of array.
# User input
# k : 10
# Array Length: 9
print("-----------------------")