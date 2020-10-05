#An example showing the working of @classmethod

class Employee:
    """A @classmethod example"""
    def __init__(self, fname, lname, age, position):
        self. fname = fname
        self.lname = lname
        self.age = age
        self.position = position

    def getEmail(self):
        print(f"{self.lname}.{self.fname}@cmpy.com")

    def fullname(self):
        print(f"{self.fname} {self.lname}")

    def printDetails(self):
        print(f"Name: {self.fname} {self.lname}\nAge: {self.age}\nPosition: {self.position}")
    
    @classmethod
    def createUser(cls,userStr):
        fname, lname, age, position = userStr.split("-")
        return cls(fname, lname, age, position)

print("-----------------------------")    
kiran = Employee('kiran', 'raj', 32, 'Developer')
kiran.getEmail();
kiran.fullname()
kiran.printDetails()
print("-----------------------------")
employeeStr1= "vishnu-r-25-manager"
vishnu = Employee.createUser(employeeStr1)
vishnu.getEmail();
vishnu.fullname()
vishnu.printDetails()
print("-----------------------------")

#Output
# -----------------------------
# raj.kiran@cmpy.com
# kiran raj
# Name: kiran raj
# Age: 32
# Position: Developer
# -----------------------------
# r.vishnu@cmpy.com
# vishnu r
# Name: vishnu r
# Age: 25
# Position: manager
# -----------------------------