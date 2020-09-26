# num3 = 300
# def outer():
#     num1 = 100
#     def inner():
#         num2 = 200
#         print(num1)
#         print(num2)
#         print(num3) 
#     inner()
    
#     print(num1)
#     # print(num2) name 'num2' is not defined
#     print(num3)

# outer()
# # print(num1)   name 'num1' is not defined
# # print(num2)   name 'num2' is not defined
# print(num3)

##Each scope create a seperate variable "a" 
# def innerSame():
#     a = 10
#     def innerSame():
#         a=20
#         print(a)
#         print("Inner: ", id(a))
#     innerSame()
#     print(a)
#     print("Outer: ", id(a))
# innerSame()
# a = 30
# print(a)
# print("Global: ", id(a))

#All scope access the same variable "a"
global a
a = 30
def innerSame():
    global a
    a = 10
    def innerSame():
        global a
        a=20
        print(a)
        print("Inner: ", id(a))
    innerSame()
    print(a)
    print("Outer: ", id(a))
innerSame()
print(a)
print("Global: ", id(a))