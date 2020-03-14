class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Account:
    def __init__(self, number, type, owner, balance=0):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance



class Bank():
    customers = []
    accounts = {}

    def add_customer(self, customer):
        if customer.id not in self.customers:
            x = customer.id
            self.customers.append(customer.id)
        else:
            print("Customer already exsists")
    def add_account(self, account):
        if account.number not in self.accounts:
            x = account.owner.id
            if x in self.customers:
                self.accounts[account.number] = account.balance
    def remove_account(self, account):
        if account.number in self.accounts == True:
            pop(account.number)

    def deposit(self, account, depo_amount):
        new_amount = self.accounts.get(account) + depo_amount
        self.accounts[account]=new_amount

    def withdrawal(self,account, withdraw_amount):
        new_amount = self.accounts.get(account) - withdraw_amount
        self.accounts[account] = new_amount

    def balance_inquiry(self, account):
        print(round(self.accounts.get(account),2))



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




