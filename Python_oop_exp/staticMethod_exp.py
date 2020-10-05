#An example to explain the working of Static methods 

class Employee:
    """A @static method example"""
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

    @staticmethod
    def printData(offAdd, offEmail):
        try:
            print(f"Name: {fname} {lname}\nAge: {age}\nPosition: {position}")
        except NameError:
            print("Static method does have access to instance attributes")
        print(f"Office Address: {offAdd}\nOffice Email: {offEmail}")


print("-----------------------------") 
Employee.printData("Company, Block2 Building, Trivandrum", "contact@cmpy.com")
print("-----------------------------") 
empStr1 = "kiran-raj-32-dev" 
k1 = Employee.createUser(empStr1)
k1.fullname()
k1.getEmail()
k1.printData("Company, Block2 Building, Trivandrum", "contact@cmpy.com")



# Output
# -----------------------------
# Static method does have access to instance attributes
# Office Address: Company, Block2 Building, Trivandrum
# Office Email: contact@cmpy.com
# -----------------------------
# kiran raj
# raj.kiran@cmpy.com
# Static method does have access to instance attributes
# Office Address: Company, Block2 Building, Trivandrum
# Office Email: contact@cmpy.com
