word = input("Enter a word or sentence to swap letter case : ")

def swap_case(s):
    str_to_list = list(s)
    length = len(str_to_list)
    for i in range(length):
        if str_to_list[i].islower():
            str_to_list[i] = str_to_list[i].upper()
        elif str_to_list[i].isupper():
            str_to_list[i] = str_to_list[i].lower()
    s = "".join(str_to_list)
    return s

print(swap_case(word))