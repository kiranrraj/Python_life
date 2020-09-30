variableA = "i am a global variable"
variableB = "dummy"

def myFunGlobalPrint():
    print("Inside function myFunGlobalPrint : ", variableA) #Inside function myFunGlobalPrint :  i am a global variable
myFunGlobalPrint()

def myFunNewAssign():
    variableC = 1000
    def inner():
        global variableC
        #print("variable inside before assignment :", variableC) 
        #NameError: name 'variableC' is not defined
        variableC = 2000
        print("variable inside after assignment :", variableC)#variable inside after assignment : 2000
        variableA = "New value assigned"
    print("Value before inner call :", variableC)#Value before inner call : 1000
    print("Inside : ", variableA)   #Inside : New value assigned
    inner()
    print("Value after inner call :", variableC)#Value after inner call : 1000
    print("Outer : ", variableA)    #Outer : i am a global variable
myFunNewAssign()
print(variableC)    #2000

# def myFunCreate():
#     variableA = variableA *2   
#     print(variableA)     #UnboundLocalError: local variable 'variableA' referenced before assignment
# myFunCreate()

def myFunCreateGlobal():
    global variableB
    variableB = variableB * 2   
    print(variableB)    #dummydummy
myFunCreateGlobal()

def myFunCreateNonLocal():
    xlocal = "local"
    def inner():
        nonlocal xlocal
        xlocal = "new local"
        print(xlocal)   #new local
    inner()
    print(xlocal) #new local
myFunCreateNonLocal()

def myFunMakingGlobal():
    global xGlobal
    xGlobal = "value"
    def inner():
        xGlobal = "new value assigned"
        print("Value inside : ", xGlobal)   #Value inside :  new value assigned
    inner()
    print("Value outside : ", xGlobal)  #Value outside :  value
myFunMakingGlobal()

xGlobal = "value assigned outside"
print("value global scope : ", xGlobal) #value global scope :  value assigned outside  
print("Outside : ", variableA) #Outside : i am a global variable
print(variableB)    #dummydummy

