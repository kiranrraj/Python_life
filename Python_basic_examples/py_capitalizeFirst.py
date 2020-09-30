s = input("Enter you full name in lower letter : ")
words = s.split(" ")
newWords=[]
for i in words:
    print(i)
    lenWord = len(i)
    i = i.capitalize()
    # if len(i) != lenWord:
    #     i = " "+ i
    # print(i)
    newWords.append(i)
s = " ".join(newWords)
print(s)

# ' '.join(map(str.capitalize, string.split(' ')))