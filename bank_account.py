class Bank_Account:
    all_accounts=[]
    def __init__(self,init_deposit=0,int_rate=0.5,fee_rate=5):
        self.balance=0
        self.int_rate=int_rate/100
        self.fee_rate=fee_rate
        self.deposit(init_deposit)

    def deposit(self,amount):
        self.balance+=amount
        return self

    def withdraw(self,amount):
        if Bank_Account.can_withdraw(self.balance,amount):
            self.balance-=amount
        else:
            print (f"Insufficient funds: Charging a ${self.fee_rate} fee")
            self.balance-=self.fee_rate
        return self

    def display_account_info(self,verbose=False):
        print(f"Balance : ${self.balance}")
        if verbose:
            print(f"Interest Rate : {self.int_rate*100}%")
            print(f"Fee Rate : ${self.fee_rate}/overdraft")
        print()
        return self

    def yield_interest(self):
        self.balance=round(self.balance*(1+self.int_rate))
        return self

    @staticmethod
    def can_withdraw(balance,amount):
        return balance>=amount
