from datetime import datetime

class Account:
    # name="account"
    def __init__(self,name,phone,):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transaction=[]
        self.loanLimit=8000
        self.loan=0
        self.transactions=[]
        self.transactionfee=200
        
        
        
        
    def  deposit(self,amount):
        if amount <=0:
            return "invalid"
        else:
            self.balance+=amount
            transaction={
                "amount":amount,"balance":self.balance,"narration":"you deposited","time":datetime.now()}
            self.transactions.append(transaction)

            return f"hello {self.name} you have deposited {amount} your balance is {self.balance}"


        

    def withdraw(self,amount) :
        total=amount+self.transactionfee
        if amount<=0:
            return "Please input a valid amount" 
        elif total>self.balance:
            return "insuffient  balance"
        else:
            self.balance-=total
            transaction={
                "amount":amount,"balance":self.balance,"narration":"you have withdraw","time":datetime.now()}
            self.transactions.append(transaction)

            return f"hello {self.name} you have withdraw {amount} your balance is {self.balance}"

            
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
            transaction={
                "amount":amount,"balance":self.balance,"narration":"you have borrow","time":datetime.now()}
            self.transactions.append(transaction)

            return f"hello {self.name} you have borrow {amount} your balance is {self.balance}"
    def repayment(self,amount):
        if amount>self.loan:
            excess=amount-self.loan
            self.balance+=excess
            transaction={
                "amount":amount,"balance":self.balance,"narration":"you can repay","time":datetime.now()}
            self.transactions.append(transaction)
            
            return "can repay"
        elif amount<0:
            return "you can't repay"  
        else:
            transaction={
                "amount":amount,"balance":self.balance,"narration":"repayment","time":datetime.now()}
            self.transactions.append(transaction)
            return f"hello {self.name} you have {amount} excess"



        
         
    def statement(self):
        for transaction in self.transactions:
            amount=transaction["amount"]
            narration=transaction["narration"]
            balance=transaction["balance"]
            time=transaction["time"]
            date=time.strftime("%D")
            print(f"{date}...{narration}...{amount}... balance {balance}")

        
    
          
    #          return f"{self.owner} paid water bill from {self.accountName}"
    # def send(self):
    #          return  f"money was send to {self.owner}      