'''There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0 . 
For each i integer in the array, if i element of A you add  to your happiness. If i element of B you add -1
to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain 
duplicate elements.'''

countN, countM = input().split()
arr = list(int(x) for x in input().split())#set will remove duplicate so avoid it
setA = set(int(y) for y in input().split())
setB = set(int(z) for z in input().split())
# print(setA,setB,arr)
# print(len(setA.intersection(arr)) - len(setB.intersection(arr)))
#when we use sum function in a list of bool True will get 1 and false will get zero
#sum([True, False, True, False, True, True, True]) => 5
# In the below example setA and setB is checked simultaneously with arr
print (sum([(i in setA) - (i in setB) for i in arr]))