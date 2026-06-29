class Bankaccount:
    def __init__(self,balance,name):
        self.name=name
        self._balance=balance
    
    def get_balance(self):
        return self.__balance
    #Setters
    def set_balance(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("INVALID BALANCE AMOUNT")
    
account=Bankaccount(500,"RIYA") 
print(account.get_balance())
account.set_balance(500)
print("Total after adding",account.get_balance())
