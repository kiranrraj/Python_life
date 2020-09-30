
while True :
    try:
        user_limit = int(input("Enter the length of the list: "))
        user_search = int(input("Enter the element you wish to search: "))
        break
    except ValueError:
        print("Try again with a numeric type")
        continue

def getUserElem(ul):
    user_list = []
    for i in range(ul):
        user_elem = input('Enter the number: ')
        if(user_elem.isnumeric()):
            user_list.append(int(user_elem))
        else:
            print(f"You entered {user_elem}.\nPlease enter a number.")
            break
    return user_list
    
def searchElem(usearch):
    found=False
    user_list = getUserElem(user_limit)
    for j in range(len(user_list)):
        if user_list[j] == usearch:
            print(f"Found {usearch} at index {j+1}")
        # print(user_list[j], usearch)
            found = True
            break
    if found == False:
        print(f"Sorry, {usearch} not found")

searchElem(user_search)    