def small_large(arr):
    length = len(arr)
    sorted_arr = sorted(arr)
    print(f"The smallest number in the array {arr} is {sorted_arr[0]} ")
    print(f"The largest number in the array {arr} is {sorted_arr[length-1]} ")

num = [44,66,2,55,77,99,4,2,11,90,60,45,23,34,47,34]

small_large(num)