from model.branch import Branch
from model.employee import Employee
from model.customer import Customer

class Bank:
    
    name = 'Bank im.Ziemowita Andrzejewskiego'    
    branches = 0
    employees = 0

    customers = 0
    deposit = 0
    interest = 0

    def __init__(self):
        self.calculate_branches()
        self.calculate_employees()
        self.calculate_customers()
        self.calculate_deposit()
        self.calculate_interest()

    @classmethod
    def calculate_branches(cls):
        cls.branches = len(Branch.all_branches)
        return cls.branches

    @classmethod
    def calculate_employees(cls):
        cls.employees = len(Employee.all_employees)
        return cls.employees

    @classmethod
    def calculate_customers(cls):
        cls.customers = len(Customer.all_customers)
        return cls.customers

    @classmethod
    def calculate_deposit(cls):
        amount = 0
        for branch in Branch.all_branches:
            amount += branch.calculate_branch_deposit()
        cls.deposit = amount
        return cls.deposit

    @classmethod
    def calculate_interest(cls):
        amount = 0
        for branch in Branch.all_branches:
            amount += branch.calculate_branch_interest()     
        cls.interest = amount
        return cls.interest

    @classmethod
    def __str__(cls):
        return "{}\nbranches:{}\nemployees:{}\ncustomers:{}\ndeposit:{}\ninterest:{}".format(cls.name, cls.branches, cls.employees, cls.customers, cls.deposit, cls.interest)
