import sys


def find_palingram(txt_in):

    outlist = []
    with open(txt_in) as file:
        words_list = file.read().strip().lower().split('\n')
        word_list = [word for word in words_list if len(word) > 1]
        for word in word_list:
            reverse = word[::-1]
            length = len(word)
            if length > 1:
                for i in range(length):
                    if word[i:] == reverse[:length-i] and reverse[length-i:] in word_list:
                        outlist.append((word, reverse[length-i:]))
                    if word[:i] == reverse[length-i:] and reverse[:length-i] in word_list:
                        outlist.append((reverse[:length-i], word))
    print(outlist)
    print(len(outlist))


find_palingram('words.txt')
