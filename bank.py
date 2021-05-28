class Bank:
    name="account"
    def __init__(self,accountName,owner,accountNumber,):
        self.accountName=accountName
        self.owner=owner
        self.accountNumber=accountNumber
        
    def  deposit(self):
          return f" 5000ksh was withdrawal from account number {self.accountNumber} by {self.owner}"
    def pay(self):
             return f"{self.owner} paid water bill from {self.accountName}"
    def send(self):
             return  f"money was send to {self.owner}"       