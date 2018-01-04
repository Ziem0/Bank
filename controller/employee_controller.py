import datetime
from controller.central import Central
from model.customer import Customer
from model.credit import Credit
from model.account_limit import AccountLimit

class EmployeeController(Central):

    def __init__(self, ui, user, dao):
        self.ui = ui
        self.user = user
        self.dao = dao
        self.start_controller()

    def handle_menu(self):
        if self.choice == len(self.ui.menu):
            self.start = 0
            self.ui.clear()
        elif self.choice == 1:
            self.ui.clear()
            self.show_my_customers()
        elif self.choice == 2:
            self.ui.clear()
            self.add_new_customer()
        elif self.choice == 3:
            self.ui.clear()
            self.choose_customers()
        elif self.choice == 4:
            self.ui.clear()
            commission = self.user.calculate_commission()
            self.ui.print('Total:{} Earnings:{} Commission:{}'.format(commission+self.user.earnings, self.user.earnings, commission))

    def show_my_customers(self):
        self.ui.print(self.ui.create_menu(self.ui.title3, self.user.customers))

    def add_new_customer(self):
        name, password = self.ui.login_inputs()
        surname, birth, earnings = self.ui.new_customer_inputs()
        customer = Customer(self.user.director, self.user, earnings, name, surname, birth)
        self.dao.save_password_new_person(name, password)        

    def choose_customers(self):
        menu = [customer.__class__.__name__ for customer in self.user.customers]
        self.ui.print(self.ui.create_menu(self.ui.title3, [customer.name+' '+customer.surname for customer in self.user.customers]))
        choice = self.ui.user_choice(menu)
        self.customer = self.user.customers[choice-1]
        self.customer_menu()

    def customer_menu(self):
        while 1:
            self.ui.print(self.ui.create_menu(self.ui.title2, self.ui.menu1))
            choice = self.ui.user_choice(self.ui.menu1)
            self.handle_customer_actions(choice)
            break 

    def handle_customer_actions(self, choice):
        if choice == 1:
            account = self.customer.add_account()
        elif choice == 2:
            self.choose_new_product()
        elif choice == 3:
            return
    
    def choose_new_product(self):
        self.ui.print(self.ui.create_menu(self.ui.title4, self.ui.menu2))
        choice = self.ui.user_choice(self.ui.menu2)
        self.create_new_product(choice)

    def create_new_product(self, choice):
        if choice == 1:
            amount_of_credit, period = self.ui.new_credit_inputs()
            add_product = Credit(amount_of_credit, period)
            add_product.start_date = datetime.date.today()
        elif choice == 2:
            amount = self.ui.new_creditflex_inputs()
            add_product = AccountLimit(amount)

        self.customer.account.assign_credit_amount_to_account(add_product)            
