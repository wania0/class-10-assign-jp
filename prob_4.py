# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

# Solution :

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance):
        if account_number in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[account_number] = {
                'account_holder': account_holder,
                'balance': initial_balance
            }
            print("Account for", account_holder, "created successfully!")

    def debit(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] = self.accounts[account_number]['balance']- amount
                print("Debited", amount, "from account", account_number,"New balance is", self.accounts[account_number]['balance'])
            else:
                print("Balance is not enough for debit!")
        else:
            print("Account does not exist!")

    def credit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] = self.accounts[account_number]['balance'] + amount
            print("Created", amount, "in account", account_number,"New balance is", self.accounts[account_number]['balance'])
        else:
            print("Account does not exist!")

    def get_balance(self, account_number):
        if account_number in self.accounts:
            print("The balance is:", self.accounts[account_number]['balance'])
        else:
            print("Account does not exist!")

# instance 
bank = Bank()

#Create acc
bank.create_account('123456', 'Mark', 500)
bank.get_balance('123456')

#Create acc
bank.create_account('789101', 'Shane', 1000)
bank.get_balance('789101')

# amount withdraw  
bank.debit('123456', 100)
bank.get_balance('123456')

# amount added
bank.credit('789101', 200)
bank.get_balance('789101')


