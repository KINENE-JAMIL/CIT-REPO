class BankAccount:
    def __init__(self,account_number,balance,owner,Type):
        self.account_number=str(account_number)
        self.balance=float(balance)
        self.owner=str(owner)
        self.Type=str(Type)
        
    def __repr__(self):
        return f"Account Number;{self.account_number} \n Balance; {self.balance}"


class Bank:
    def __init__(self,name,accounts):
        self.name=str(name)
        self.accounts=accounts
    
    def __repr__(self):
        return f"Bank Name: {self.name}"
    
    def add_account(self,account):
        self.accounts.append(account)


class Customer:
    def __init__(self,name,accounts):
        self.name=str(name)
        self.accounts=accounts
        
    def __repr__(self):
        return f"Customer Name: {self.name}"
    
    def add_account(self, account):
        self.accounts.append(account)


class Transactions:
    def __init__(self,account,amount,Type):
        self.account=str(account)
        self.amount=float(amount)
        self.Type=str(Type)
        
    def transacting(self):
        if self.Type=="C":
            self.account.balance=self.account.balance+self.amount
        if self.Type=="D" and self.account.balance >=self.amount:
            self.account.balance=self.account.balance-self.amount

# CREATE BANK
bank=Bank("JPMorgan",[])

# customer
customer= Customer("kinene",[])

# bank account
Account=BankAccount("10321098909",159.8,"kinene","USD_Savings")

# adding BankAccount to the Bank
Bank.add_account(Account)

# adding BankAccount to Customer
Customer.add_account(Account)

print(bank)

print(customer)