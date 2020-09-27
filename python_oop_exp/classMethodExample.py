class BankAccount:
    """A class that accept user details for a bank"""

    def __init__(self, custName, custEmail, custPhone):
        self.custName = custName
        self.custEmail = custEmail
        self.custPhone = custPhone
    
    def printDetails(self):
        print(f"Name : {self.custName}\nEmail : {self.custEmail}\nPhone : {self.custPhone}")
        
kiran = BankAccount("kiran raj r", "kiran@gmail.com", 2244)
kiran.printDetails()

#Using class method

class BankAccountCM:
    """A class that accept user details for a bank"""

    def __init__(self, custName, custEmail, custPhone):
        self.custName = custName
        self.custEmail = custEmail
        self.custPhone = custPhone

    @classmethod
    def from_Init(cls, custStr):
        custName, custEmail, custPh = custStr.split('-')
        cls.custName = custName
        cls.custEmail = custEmail
        cls.custPh = custPh
        return cls(custName, custEmail, custPh)

    @classmethod
    def printDetails(cls):
        print(f"Name : {cls.custName}\nEmail : {cls.custEmail}\nPhone : {cls.custPh}")

cust1 = "vish-vishnuvjd@gmail-223322"

vishnu = BankAccountCM.from_Init(cust1)
print(vishnu.__dict__)
BankAccountCM.printDetails()
vishnu.printDetails()