class Account:
    # name="account"
    def __init__(self,name,phone,):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transaction=100
        self.loanLimit=8000
        self.loan=0
        
        
        
    def  deposit(self,amount):
        if amount <=0:
            return "invalid"
        else:
            self.balance+=amount
            return f"hello {self.name} you have deposited {amount} your balance is {self.balance}"

        

    def withdraw(self,amount) :
        total=amount+self.transaction
        if amount<=0:
            return "Please input a valid amount" 
        elif total>self.balance:
            return "insuffient  balance"
        else:
            self.balance-=total
            return f"hello {self.name} you have withdraw {self.amount} and you balance is {self.balance}"
    def borrow(self,amount) :
        if amount<0:
            return "can't borrow" 
        elif self.loan>0: 
            return "can not borrow"  
        elif amount>self.loanLimit:
            return "you can not borrow" 
        else:
            fees=0.05*amount
            self.balance+=amount
            self.loan=amount+fees
            return f"hello {self.name} you have withdraw {amount} and your balance is {self. balance}"


        
    
          
    #          return f"{self.owner} paid water bill from {self.accountName}"
    # def send(self):
    #          return  f"money was send to {self.owner}      