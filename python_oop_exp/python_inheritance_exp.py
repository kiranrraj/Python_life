import random
import math

class Employee:

    defaultraise = 1.15
    totalSalary = 0
    
    def __init__(self, fname, lname, email, ph, bSalary):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.ph = ph
        self.bSalary = bSalary

    def printDetails(self):
        print(f"Name : {self.fname} {self.lname}\nEmail: {self.email}\nPhone no: {self.ph}")
    
    def customEmail(self):
        custEmail = self.fname + "." + self.lname + str(math.ceil(random.random() *100)) + "@company.com"
        return custEmail

    def getSalary(self):
        self.totalSalary = self.bSalary + (self.bSalary * 0.6) 
        return self.totalSalary
   
    def payRaise( self):
        self.bSalary = int(self.bSalary * self.defaultraise)
        return self.bSalary

kiran = Employee('Kiran', 'Raj', 'kiranrajvjd@gmail.com', 2444, 30000)
vishnu = Employee('Vishnu', 'R', 'vishvjd@gmail.com', 2664, 50000)

kiran.printDetails()
print(kiran.customEmail())
print(kiran.getSalary())
kiran.payRaise()
print(kiran.getSalary())
print("##------------------##")
vishnu.printDetails()
print(vishnu.customEmail())
print(vishnu.getSalary())
vishnu.payRaise()
print(vishnu.getSalary())
print("##------------------##")

class Developer(Employee):
    defaultraise = 1.20

    def __init__(self, fname, lname, email, ph, bSalary,Devtype):
        super().__init__(fname, lname,email, ph, bSalary)
        #Employee.__init(self,fname, lname,email, ph, bSalary)
        self.Devtype = Devtype

    def printDetails(self):
        super().printDetails()
        print(f"Developer Type: {self.Devtype}")

    def payRaise(self):
        self.bSalary = int(self.bSalary * self.defaultraise)
        return self.bSalary

kiranDev = Developer('Kiran', 'Raj', 'kiranrajvjd@gmail.com', 2444, 30000, "Tester")
kiranDev.printDetails()
print(kiranDev.getSalary())
kiranDev.payRaise()
print(kiranDev.getSalary())
print(kiranDev.customEmail())