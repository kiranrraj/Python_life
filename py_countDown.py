user_input = input("Enter a number to count down :")

def countDown(x):
    if x==0:
        print("Lift off")
    else:
        print(x)
        countDown(x-1)

intVal = int(user_input)
countDown(intVal)