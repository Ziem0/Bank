from controller.central import Central
from model.employee import Employee

class DirectorController(Central):
    
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
            self.show_my_employees()
        elif self.choice == 2:
            self.ui.clear()
            self.show_my_customers()
        elif self.choice == 3:
            self.ui.clear()
            self.add_new_employee()
        elif self.choice == 4:
            self.ui.clear()
            self.ui.print(self.show_branch_interest())
        elif self.choice == 5:
            self.ui.clear()
            self.ui.print(self.show_branch_deposit())

    def show_my_employees(self):
        self.ui.print(self.ui.create_menu(self.ui.title2, [employee for employee in self.user.employees]))

    def show_my_customers(self):
        self.ui.print(self.ui.create_menu(self.ui.title3, [employee for employee in self.user.customers]))

    def show_branch_interest(self):
        interest = self.user.branch.calculate_branch_interest()
        return interest

    def show_branch_deposit(self):
        deposit = self.user.branch.calculate_branch_deposit()
        return deposit
        
    def add_new_employee(self):
        name, password = self.ui.login_inputs()
        surname, birth, earnings = self.ui.new_employee_inputs()
        customer = Employee(self.user, earnings, name, surname, birth)
        self.dao.save_password_new_person(name, password)        
