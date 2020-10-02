def find_mean(arr):
    length = len(arr)
    sumArr = 0
    for i in arr:
        sumArr+=i
    print(f"The mean of the arr{arr} is {sumArr/length} ")

num = [44,66,2,55,77,99,4,2,11,90,60,45,23,34,47,34] 
find_mean(num)
#The mean of the arr[44, 66, 2, 55, 77, 99, 4, 2, 11, 90, 60, 45, 23, 34, 47, 34] is 43.3125 

num = [11,12,13,14,15] 
find_mean(num)
#The mean of the arr[11, 12, 13, 14, 15] is 13.0