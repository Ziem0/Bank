from model.product import Product

class Branch:
    
    all_branches = []
    number = 1

    def __init__(self, town):
        self.town = town
        self.number = str(Branch.number) 

        Branch.all_branches.append(self)
        Branch.number += 1

    def assign_director(self, director):
        self.director = director
        return self.director

    def create_unique(self):
        unique = self.town + self.number
        return unique

    def calculate_employees(self):
        return len(self.director.employees)

    def calculate_customers(self):
        return len(self.director.customers)

    def calculate_branch_deposit(self):
        deposit = 0
        for customer in self.director.customers:
            add = customer.account.balance
            deposit += add
        return deposit            

    def calculate_branch_interest(self):
        interest = 0
        for product, properties in Product.all_products.items():
            interest += properties[1]
        return interest

    def __str__(self):
        return "town:{}\nnumber:{}".format(self.town, self.number)

    