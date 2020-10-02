

def sum_pair(arr1, arr2, num=0):
    """This functions creates a pair(x,y) from two array
    x from array1 and y from array2 and prints the pairs in such 
    a way that they are sorted based on their sum of elements(x+y).
    You can provide an optional argument to limit the number of 
    smallest pairs to be printed"""
    
    arr_pair = []

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            arr_pair.append((arr1[i],arr2[j]))
            # print(i,j)
    
    for i in range(len(arr_pair)):
        for j in range(i+1,len(arr_pair)):
            if sum(arr_pair[j]) < sum(arr_pair[i]):
                arr_pair[j], arr_pair[i] = arr_pair[i], arr_pair[j] 
    

    if num != 0:
        print(arr_pair[:num])
    else:
        print(arr_pair)

num1 = [1,2,3]
num2 = [4,5,6]

sum_pair(num1,num2)
# [(1, 4), (1, 5), (2, 4), (1, 6), (2, 5), (3, 4), (2, 6), (3, 5), (3, 6)]

#To find the first three smallest pairs 
sum_pair(num1, num2, 2) #[(1, 4), (1, 5)]



