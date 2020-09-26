class CreditCard:
    """Sample credit card details of a customer"""

    custLimit = 100000

    def __init__(self, custName, custBank, custCardType, custAcnt, custDebit):
        self.custName = custName
        self.custBank = custBank
        self.custCardType = custCardType
        self.custAcnt = custAcnt
        self.custDebit = custDebit
    
    def getBalance(self):
        print(f"Current Balance : {self.custLimit -  self.custDebit} Rs.")
    
    def getCustDetails(self):
        msg = f"Name : {self.custName}\nAccount : {self.custAcnt}\nBank : {self.custBank}\nCard Type : {self.custCardType}"
        print(msg)

kiran = CreditCard('Kiran', "HDFC", "Gold", "Savings", 15000)
kiran.getBalance()
kiran.getCustDetails()