num = [5,6,3,7,11,8,18,9,100,1,2]

def customSort(arr, algo):
    algo = algo.lower().strip()

    if algo == "ascn":
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j] < arr[i]:
                    arr[j], arr[i] = arr[i], arr[j] 
        return arr
        
    elif algo == "desc":
        for i in range(len(arr)):
             for j in range(i+1,len(arr)):
                if arr[j] > arr[i]:
                    arr[j], arr[i] = arr[i], arr[j] 
        return arr
    else:
        print("Algorithm should be 'ascn' or 'desc'")

print(customSort(num, "ascn"))
print(customSort(num, "desc"))