#An example showing the working of @classmethod

class Employee:
    """A @classmethod example"""

    companyName = "rubyRed"

    def __init__(self, fname, lname, age, position):
        self. fname = fname
        self.lname = lname
        self.age = age
        self.position = position

    def getEmail(self):
        print(f"{self.lname}.{self.fname}@{self.companyName}.com")

    def fullname(self):
        print(f"{self.fname} {self.lname}")

    def printDetails(self):
        print(f"Name: {self.fname} {self.lname}\nAge: {self.age}\nPosition: {self.position}")
    
    @classmethod
    def createUser(cls,userStr):
        fname, lname, age, position = userStr.split("-") 
        return cls(fname, lname, age, position)

    @classmethod
    def getCompany(cls):
        try:
            print(f"Name: {self.fname} {self.lname}\nAge: {self.age}\nPosition: {self.position}")
        except NameError:
            print('Cannot access instance attribute.', end=" ")

        print(f"Can only access class attributes\nCompany Name : {cls.companyName}") 

print("-----------------------------")         
Employee.getCompany()
print("-----------------------------")    
kiran = Employee('kiran', 'raj', 32, 'Developer')
kiran.getCompany()
kiran.getEmail();
kiran.fullname()
kiran.printDetails()
print("-----------------------------")
employeeStr1= "vishnu-r-25-manager"
vishnu = Employee.createUser(employeeStr1)
vishnu.getCompany()
vishnu.getEmail();
vishnu.fullname()
vishnu.printDetails()
print("-----------------------------")

#Output
# -----------------------------
# Cannot access instance attribute. Can only access class attributes
# Company Name : rubyRed
# -----------------------------
# Cannot access instance attribute. Can only access class attributes
# Company Name : rubyRed
# raj.kiran@rubyRed.com
# kiran raj
# Name: kiran raj
# Age: 32
# Position: Developer
# -----------------------------
# Cannot access instance attribute. Can only access class attributes
# Company Name : rubyRed
# r.vishnu@rubyRed.com
# vishnu r
# Name: vishnu r
# Age: 25
# Position: manager
# -----------------------------