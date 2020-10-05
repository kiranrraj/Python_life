class CreditCard:
    """A simple python oop example"""
    
    custLimitSilver = 50000
    custLimitGold = 75000
    custLimitPlatinum = 100000
    custLimit = 0
    balance = 0

    def __init__(self, custName, custBank, custAcntType, custCCType, custDebit):
        self.custName = custName
        self.custBank = custBank
        self.custAcntType = custAcntType
        self.custCCType = custCCType
        self.custDebit = custDebit

    def printDetails(self):
        msg = f"Name : {self.custName}\nBank : {self.custBank}\nAccount Type : {self.custAcntType}\nCard Type : {self.custCCType}"
        print(msg)
    
    def getLimit(self):
        if self.custCCType.lower() == "silver":
            self.custLimit = self.custLimitSilver
        elif self.custCCType.lower() == "gold":
            self.custLimit = self.custLimitGold
        elif self.custCCType.lower() == "platinum":
            self.custLimit = self.custLimitPlatinum
        else:
            print("Error occurred!!\n Enterd wrong credit card type ")
        return self.custLimit

    def calcBalance(self):
        self.balance = self.getLimit() - self.custDebit
        return self.balance
    
    def getBalance(self):
        print(f"Your current balance is {self.calcBalance()}")

    def amountToPay(self):
        print(f"Amount to be paid : {self.custDebit}")

    def purchase(self, amt):
        if amt > self.calcBalance():
            print(f"Sorry you exceeded your limit.\nYour limit is {self.calcBalance()}")
        else:
            self.custDebit = self.custDebit + amt
            return self.custDebit

    def payAmount(self, amt):
        if self.custDebit == 0:
            print("There is no due for you, Thank You!")
        elif amt > self.custDebit:
            print(f"You can only pay Rs. {self.custDebit}")
            self.amountToPay()
        else :
            self.custDebit = self.custDebit - amt
            print(f"You paid {amt}.")
            self.amountToPay()
            return self.custDebit


kiran = CreditCard("Kiran", "HDFC", "Savings", "Platinum", 10000)
kiran.printDetails()
print("------------------------------")
kiran.getBalance()
kiran.amountToPay()
print("------------------------------")
kiran.payAmount(5000)
kiran.getBalance()
print("------------------------------")
kiran.payAmount(6000)
kiran.getBalance()
print("------------------------------")
kiran.payAmount(5000)
kiran.getBalance()
print("------------------------------")
kiran.purchase(1000)
kiran.purchase(1000)
kiran.purchase(1000)
kiran.purchase(100000)
print("------------------------------")
kiran.payAmount(5000)
kiran.getBalance()
print("------------------------------")
kiran.payAmount(3000)
kiran.getBalance()
print("------------------------------")
kiran.payAmount(3000)
kiran.getBalance()
print("------------------------------")
