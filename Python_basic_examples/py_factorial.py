user_input = input("Enter the number you want factorial of :")
num = int(user_input)

def fact(n):
    if n == 0:
        result = 1
        return result
    else:
        recursive = fact(n-1)
        result = n * recursive
        return result

print(fact(num))