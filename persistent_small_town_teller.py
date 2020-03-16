class Person:
    def __init__(self, id: int, first_name: str, last_name: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Account:
    def __init__(self, number: int, type: str, owner: Person, balance: int = 0):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance


class Bank():
    customers = {}
    accounts = {}

    def add_customer(self, customer: Person):
        if customer.id not in self.customers:
            x = customer.id
            self.customers[customer.id] = customer

        else:
            print("Customer already exsists")

    def add_account(self, account: Account):
        if account.number not in self.accounts:
            x = account.owner.id
            if x in self.customers:
                self.accounts[account.number] = accounts
            else:
                raise TypeError("Customer not registered")
        else:
            raise TypeError("This account is already created")

    def remove_account(self, account: int):
        if account.number in self.accounts == True:
            pop(account.number)

    def deposit(self, account: Account, deposit_amount: int):
        new_amount = self.accounts.get(account).balance + deposit_amount
        self.accounts[account].balance = new_amount

    def withdrawal(self, account: int, withdraw_amount: int):
        new_amount = self.accounts.get(account).balance - withdraw_amount
        self.accounts[account].balance = new_amount

    def balance_inquiry(self, account: int):
        print(round(self.accounts.get(account).balance),2)

    def save_data(self):
        PersistenceUtils.write_pickle(customers.pickle, customers)
        PersistenceUtils.write_pickle(accounts.pickle, accounts)

    def load_pickle(self):
        PersistenceUtils.load_pickle(customers.pickle)
        PersistenceUtils.load_pickle(accounts.pickle)


class PersistenceUtils():
    def __int__(self):
        pass

    @staticmethod
    def write_pickle(file_path, data):
        with open(file_path, "wb") as handler:
            pickle.dump(data, handler)

    @staticmethod
    def load_pickle(file_path):
        with open(file_path, 'rb') as handler:
            data = pickle.load(handler)
        return data


zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
zc_bank.add_customer(bob)
bob_savings = Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob_savings)
zc_bank.balance_inquiry(1001)
# 0
zc_bank.deposit(1001, 256.02)
zc_bank.balance_inquiry(1001)
# 256.02
zc_bank.withdrawal(1001, 128)
zc_bank.balance_inquiry(1001)




