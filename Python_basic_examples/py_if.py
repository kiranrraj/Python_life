msg = """If you are a good person enter y
else enter n, if you dont know enter idn : """
good_person = input(msg)

if good_person == 'y':
    print("Yes, you are a good person.")
elif good_person == 'n':
    print("You are a good person believe me.")
elif good_person == "idn":
    print("I know you are a good person.")
else:
    print("Please enter a valid input.")