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
        try :
            amount+10
        except TypeError:
            return f"please enter your amount in figures "
        if amount <=0:
            return "invalid"
        else:
            self.balance+=amount
            transaction={
                "amount":amount,"balance":self.balance,"narration":"you deposited","time":datetime.now()}
            self.transactions.append(transaction)

            return f"hello {self.name} you have deposited {amount} your balance is {self.balance}"


        

    def withdraw(self,amount) :
        try :
            amount+200
        except TypeError:
            return f"please enter your amount in figures "
        if amount <=0:
            return "invalid"
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
        try :
            amount+10
        except TypeError:
            return f"Can't withdraw "
        if amount <=0:
            return "invalid"
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
        try :
            amount+100
        except TypeError:
            return f"please enter your amount in figures "
        if amount <=0:
            return "invalid"
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
            diff=self.loan-amount
            transaction={
                "amount":amount,"balance":self.balance,"narration":"repayment","time":datetime.now()}
            self.transactions.append(transaction)
            return f"hello {self.name} you have {amount} excess"
        
    def transfer(self,amount,account):
        try :
            amount+100
        except TypeError:
            return f"please enter  a number "
            fee=amount*0.05
            total=amount+fee

        if amount>=0:
            return " amount should be more than 0"
        if total>self.balance:
            return f"hello your balance is {self.balance}"
            
         
        else:
            self.balance-=total
            account.deposit(amount)
            return f"you have successful transfer{self.amount} to {self.Account} "

        
         
    def statement(self):
        for transaction in self.transactions:
            amount=transaction["amount"]
            narration=transaction["narration"]
            balance=transaction["balance"]
            time=transaction["time"]
            date=time.strftime("%D")
            print(f"{date}...{narration}...{amount}... balance {balance}")

        
class MobileMoneyAccount(Account):
    def __init__(self,name,phone,serviceprovider):
         Account.__init__(self,name,phone)
         self.serviceprovider=serviceprovider


    def buy_airtime(self,amount,account):

        if amount<=0:
            return f"you cannot buy airtime"
        if amount>self.balance:
            
            return f"you have insuffient balance" 

        
            
        else:
            self.balance-=amount
            account.deposit(amount)
            transaction={"amount":amount,"balance":self.balance,"narration":"you buy airtime on ","time":datetime.now()}
            self.transactions.append(transaction)
            return f"you have successful bought {amount} of airtime and your balance is {self.balance} "   

              
        
        