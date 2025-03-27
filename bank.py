class Person():
    def __init__(self, name, personal_code):
        self.name = name
        self.personal_code = personal_code
        self.accounts = []
    
    
    def add_account(self, accounts):
        self.accounts.append(account)
        

    def get_accounts():
        for account in self.__accounts:
            print(account)
        return(self.accounts)
    
    def get_info(self):
        return f"Username: {self.name}, Password: {self.personal_code}"
    
    
class BankAccount():
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
        
    
    def add(self, amount):
        self.balance += amount
        

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("You don't have enough money")
    
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    
account1 = Person("dasa", 1234)
print(account1.get_info())

account1 = BankAccount("001", 100)
account1.add_account(account1)
account1.get_accounts()
