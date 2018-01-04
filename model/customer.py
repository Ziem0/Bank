from model.person import Person
from model.account import Account

class Customer(Person):
    
    all_customers = []

    def __init__(self, director, employee, earnings, *args, account='No account'):
        self.director = director
        self.employee = employee
        self.earnings = earnings
        self.account = account
        super().__init__(*args)

        self.director.add_customer(self)
        self.employee.add_customer(self)
        Customer.all_customers.append(self)

    def add_account(self):
        unique = self.name+self.surname+self.director.branch.create_unique()
        self.account = Account(unique)        
        return self.account

    def __str__(self):
        return "name:{}\nsurname:{}\naccount:{}\nemployee:{}\nbranch:{}\n".format(self.name, self.surname, self.account, self.employee.surname, self.director.branch.create_unique())

    