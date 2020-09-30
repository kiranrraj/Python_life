import sys

user_limit = input("Enter the length of the list: ")

if not user_limit.isnumeric():
    print(f"Length shoud be whole number greater than 0, receiver '{user_limit}' of type {type(user_limit)}.")
    sys.exit()

user_limit= int(user_limit)
user_search = input("Enter the element you wish to search: ").strip()


def getUserElem(ul):
    user_list = []
    for i in range(ul):
        user_elem = input('Enter the element: ').strip()
        user_list.append(user_elem)
    return user_list

def searchElem(usearch):
    found=False
    user_list = getUserElem(user_limit)
    for j in range(len(user_list)):
        if user_list[j] == usearch:
            print(f"Found {usearch} at index {j+1}")
            found = True
            break
    if found == False:
        print(f"Sorry, {usearch} not found")

searchElem(user_search)
