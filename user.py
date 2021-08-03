from bank_account import Bank_Account
class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.accounts=[]
        self.create_new_account()
    def make_deposit(self,amount,account_index):
        self.accounts[account_index].deposit(amount)
        return self
    def make_withdrawl(self,amount,account_index):
        self.accounts[account_index].withdraw(amount)
        return self
    def display_user_balance(self,account_index,verbose=False):
        self.accounts[account_index].display_account_info(verbose)
    def create_new_account(self, intial_deposit=0, int_rate=0.5, fee_rate=5):
        new_account=Bank_Account(intial_deposit,int_rate,fee_rate)
        self.accounts.append(new_account)
    def display_all_accounts(self,verbose=False):
        for i,account in enumerate(self.accounts):
            print(f"Account {i}")
            account.display_account_info(verbose)


wesley=User("Wesley","Wesley.giles@gmail.com")
wesley.make_deposit(400,0)
wesley.create_new_account(500000,1)
wesley.display_all_accounts()