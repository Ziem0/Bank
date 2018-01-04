import os, sys
import csv
import datetime
from model.bank import Bank
from controller.central import Central
from controller.bank_controller import BankController
from controller.director_controller import DirectorController
from controller.employee_controller import EmployeeController
from controller.customer_controller import CustomerController
from controller.account_controller import AccountController
from ui.ui import UI
from ui.bank_ui import BankUI
from ui.director_ui import DirectorUI
from ui.employee_ui import EmployeeUI
from ui.customer_ui import CustomerUI
from ui.account_ui import AccountUI

class Controller(Central):
    
    def __init__(self, ui, dao):
        self.ui = ui
        self.dao = dao
        self.bank_ui = BankUI()
        self.director_ui = DirectorUI()
        self.employee_ui = EmployeeUI()
        self.customer_ui = CustomerUI()

        self.dao.create_data()
        self.ui.clear()
        self.start_controller()

    def handle_menu(self):
        if self.choice == len(self.ui.menu):
            self.dao.save_data()
            self.dao.save_password()
            sys.exit('GoodBye')
        else:
            self.ui.clear()
            self.login()

    def pick_controller(self):
        if self.choice == 1:
            self.ui.clear()
            BankController(self.bank_ui)
        if self.choice == 2:
            self.ui.clear()
            DirectorController(self.director_ui, self.user, self.dao)
        if self.choice == 3:
            self.ui.clear()
            EmployeeController(self.employee_ui, self.user, self.dao)
        if self.choice == 4:
            self.ui.clear()
            CustomerController(self.customer_ui, self.user)