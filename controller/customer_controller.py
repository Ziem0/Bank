from controller.central import Central
from model.account import Account
from model.product import Product

class CustomerController(Central):
    def __init__(self, ui, user):
        self.ui = ui
        self.user = user
        self.ui.clear()
        self.start_controller()
    
    def handle_menu(self):
        if self.choice == len(self.ui.menu):
            self.start = 0
            self.ui.clear()
        elif self.choice == 1:
            self.ui.clear()
            self.ui.print("Account balance: {}".format(self.user.account.balance))
            self.ui.print(self.user.account.account_limit)
            self.ui.print("Taken credit: {}".format(self.user.account.credit_balance))
        elif self.choice == 2:
            self.ui.clear()
            amount = self.ui.cash_in_out_inputs()
            self.user.account.cash_in(amount)
        elif self.choice == 3:
            self.ui.clear()
            amount = self.ui.cash_in_out_inputs()
            self.cash_out(amount)
        elif self.choice == 4:
            self.ui.clear()
            self.ui.print(self.show_monthly_repayment())
        elif self.choice == 5:
            self.ui.clear()
            self.choose_product()
        elif self.choice == 6:
            self.ui.clear()
            self.use_limit()

    def show_monthly_repayment(self):
        to_pay = 0
        for product in self.user.account.products:
            if isinstance(product, Product):
                to_pay += product.calculate_monthly_repayment()
        return to_pay

    def choose_product(self):
        products = [product.__class__.__name__ for product in self.user.account.products]
        self.ui.print(self.ui.create_menu(self.ui.title5, products))
        self.choice_product = self.user.account.products[self.ui.user_choice(products)-1]
        self.handle_products()

    def handle_products(self):
        if self.choice_product.__class__.__name__ == 'Credit': 
            return self.repaid_credit()
        else:
            return self.repaid_credit_flex()

    def repaid_credit(self):
        cash_to_pay = self.choice_product.automatical_monthly_repayment()
        if cash_to_pay < self.user.account.balance:
            if cash_to_pay > 0:
                self.user.account.balance -= cash_to_pay
                self.choice_product.amount_of_credit += (self.choice_product.amount_of_credit / self.choice_product.period)
                self.user.account.credit_balance += (self.choice_product.amount_of_credit / self.choice_product.period) 
            if self.choice_product.amount_of_credit == 0:
                self.user.account.products.remove(self.choice_product)
        else:
            self.ui.print(self.ui.title2)

    def repaid_credit_flex(self):
        self.choice_product.set_date_repayment()
        cash_to_pay = self.choice_product.calculate_repayment()    
        if cash_to_pay < self.user.account.balance:
            self.user.account.balance -= cash_to_pay
            self.user.account.account_limit = "+ Account Limit: {}\n+ Used credit: {}".format(self.choice_product.amount_of_credit, self.choice_product.amount_of_credit_used) 
            
        else:
            self.ui.print(self.ui.title2)

    def use_limit(self):
        for product in self.user.account.products:
            if product.__class__.__name__ == 'AccountLimit':
                amount = self.ui.cash_in_out_inputs()
                if amount > product.amount_of_credit:
                    self.ui.print('{}{}\n\n'.format(self.ui.title6, product.amount_of_credit))
                else:
                    product.amount_of_credit_used += amount
                    self.user.account.balance += amount
                    self.user.account.account_limit = "+ Account Limit: {}\n+ Used credit: {}".format(product.amount_of_credit, product.amount_of_credit_used) 
                    

    def cash_out(self, amount):
        if not isinstance(amount, int):
            raise ValueError
        else:
            if amount <= self.user.account.balance:
                self.user.account.balance -= amount
                return self.user.account.balance
            else:
                self.ui.print(self.ui.title2)











But for his illnes+AHw-Gdyby nie jego choroba,,,,,,,,
Everything but this+AHw-Wszystko oprocz tego,,,,,,,,
Everyone but you+AHw-Wszyscy inni oprocz ciebie,,,,,,,,
I can but try+AHw-Moge jedynie probowac,,,,,,,,