import sys


def load_file(f_in):
    out = []
    try:
        with open(f_in) as file:
            words_list = file.read().strip().lower().split('\n')

        for word in words_list:
            if len(word) > 1 and word == word[::-1]:
                out.append(word)
        print(f"The palindrome words are : {out}")
        print(
            f"The number of palindrome words in the '{file.name}' is {len(out)} : ")

    except IOError as e:
        print(f"{e} Error opening {f_in}. Terminating program.")
    sys.exit(1)


load_file('words.txt')
