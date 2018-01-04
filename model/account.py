import datetime
from model.credit import Credit
from model.card_credit import CardCredit
from model.account_limit import AccountLimit

class Account:
    
    number = 1

    def __init__(self, unique):
        self.number = str(Account.number) + unique
        Account.number += 1
        self.balance = 0
        self.credit_balance = 0
        self.account_limit = '0'
        self.products = []

    def cash_in(self, amount):
        self.balance += amount
        return self.balance

    def add_product(self, product):
        self.products.append(product)
        return self.products[-1]
     
    def assign_credit_amount_to_account(self, product):
        if product.__class__.__name__ == 'Credit':
            if product.start_date == datetime.date.today():
                self.credit_balance -= self.add_product(product).amount_of_credit
                self.balance += product.amount_of_credit
                product.start_date = product.start_date - datetime.timedelta(1)
            else:
                self.add_product(product)               
                self.credit_balance = -(product.amount_of_credit)
                 
        else:
            self.add_product(product)
            self.account_limit = product.screen

    def __str__(self):
        return "{}\nAccount balance: {}".format(self.number, self.balance)
    