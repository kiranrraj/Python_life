class Employee:

    def __init__(self, fname, lname,companyName):
        self.fname = fname
        self.lname = lname
        self.companyName = companyName

    @property
    def fullName(self):
        return "{} {}".format(self.fname, self.lname)
    
    @property
    def getEmail(self):
        return "{}.{}@{}.com".format(self.fname, self.lname, self.companyName)

kiran = Employee('kiran', 'raj', 'google');

#Befor applying the @property decorator
# print(kiran.fullName())
# print(kiran.getEmail())

#After applying the @property decorator
#We can call methods like attribute
print(kiran.fullName)
print(kiran.getEmail)