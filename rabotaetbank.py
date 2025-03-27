class Person:
    def __init__(self, name, personal_code):
        self.name = name
        self.personal_code = personal_code
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_accounts(self):
        for account in self.accounts:
            print(account.get_account_number())
        return self.accounts

    def get_info(self):
        return f"Username: {self.name}, Password: {self.personal_code}"

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def add(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("You don't have enough money")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

class Client(Person):
    def __init__(self, name, phone, email, personal_code):
        super().__init__(name, personal_code)
        self.email = email
        self.phone = phone
        self.client_type = "Regular"  

    def account_summary(self):
        for account in self.accounts:  
            balance = account.get_balance()  
            if balance <= 1000:
                self.client_type = "Regular"
            elif balance > 10000:
                self.client_type = "Premium"
            else:
                self.client_type = "Business"
        
        
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Client Type: {self.client_type}")
        print(f"Password: {self.personal_code}")


person = Person("Dasa", 1234)
print(person.get_info())

account1 = BankAccount("001", 100)
account2 = BankAccount("002", 12000)  


person.add_account(account1)
person.add_account(account2)


elina = Client("Elina", "2673", "sjuiaw@k", 3727789)


elina.add_account(account1)
elina.add_account(account2)


person.get_accounts()


elina.account_summary()

