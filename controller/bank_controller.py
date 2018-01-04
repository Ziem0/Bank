from model.bank import Bank
from model.branch import Branch
from controller.central import Central

class BankController(Central):
    
    def __init__(self, ui):
        self.ui = ui
        self.bank = Bank()
        self.show_all_branches()
        self.start_controller()

    def handle_menu(self):
        if self.choice == len(self.ui.menu):
            self.start = 0
            self.ui.clear()
        elif self.choice == 1:
            self.ui.clear()
            self.ui.print(self.bank.branches)
        elif self.choice == 2:
            self.ui.clear()
            self.ui.print(self.bank.employees)
        elif self.choice == 3:
            self.ui.clear()
            self.ui.print(self.bank.customers)
        elif self.choice == 4:
            self.ui.clear()
            self.ui.print(self.bank.deposit)
        elif self.choice == 5:
            self.ui.clear()
            self.ui.print(self.bank.interest)
            self.ui.print(self.bank)
            
    def show_all_branches(self):
        for branch in Branch.all_branches:
            self.ui.print(branch)

    
    