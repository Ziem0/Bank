from abc import ABC, abstractmethod
from passlib.hash import sha256_crypt
import time
from model.director import Director
from model.employee import Employee
from model.customer import Customer

class Central:
    
    def start_controller(self):
        self.start = 1
        while self.start:
            self.ui.print(self.ui.create_menu(self.ui.title1, self.ui.menu))
            self.choice = self.ui.user_choice(self.ui.menu)
            self.handle_menu()

    def login(self):
        name, password = self.ui.login_inputs()
        self.passwords = self.dao.load_password()

        for director in Director.all_directors:
            for employee in Employee.all_employees:
                for customer in Customer.all_customers:
                    if director.name == name:
                        self.user = director
                        return self.end_login(name, password)
                    if employee.name == name:
                        self.user = employee
                        return self.end_login(name, password)
                    if customer.name == name:
                        self.user = customer
                        return self.end_login(name, password)

    def end_login(self, name, password):
        for name_, password_ in self.passwords.items():
            if name == name_ and sha256_crypt.verify(password, password_):
                time.sleep(1)
                print("\nCorrect password!\n")
                time.sleep(0.5)
                return self.pick_controller()
        time.sleep(1)
        print("\nWrong password..\n")        
        time.sleep(0.5)
    