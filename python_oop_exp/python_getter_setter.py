class Employee:

    def __init__(self, fname, lname,companyName):
        self.fname = fname
        self.lname = lname
        self.companyName = companyName

    @property
    def fullName(self):
        return "{} {}".format(self.fname, self.lname)

    @fullName.setter
    def fullName(self, name):
        fname, lname = name.split(" ")
        self.fname = fname
        self.lname = lname

    @fullName.deleter
    def fullName(self):
        self.fname = None
        self.lname = None
        print("Fname and lname set to None")
    
    @property
    def getEmail(self):
        return "{}.{}@{}.com".format(self.fname, self.lname, self.companyName)
    
me = Employee('kira', 'r', 'google')
print(me.getEmail)
print("--------------------")
# me.fullName = "kiran raj" 
# #AttributeError: can't set attribute

me.fullName = "kiran raj" 
print(me.fullName)
print(me.getEmail)
print("--------------------")

del me.fullName
print(me.fullName)