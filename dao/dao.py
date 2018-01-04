import csv, os, sys, datetime
from passlib.hash import sha256_crypt
from model.bank import Bank
from model.branch import Branch
from model.director import Director
from model.employee import Employee
from model.customer import Customer
from model.account import Account
from model.credit import Credit
from model.card_credit import CardCredit
from model.account_limit import AccountLimit
from model.product import Product
from model.product_flex import ProductFlex

class Dao:
    
    @staticmethod
    def create_data():
        if not os.path.isfile('static/data.csv'):
            raise FileNotFoundError 
        else:
            with open('static/data.csv', 'r', encoding='utf16') as f:
                reader = csv.reader(f)
                for i in reader:
                    for class_ in [Bank, Branch, Director, Employee, Customer, Account, Credit, CardCredit, AccountLimit]:
                        if i[0] == class_.__name__:
                            properties = [n for n in i[1:] if n]
                            for n,z in enumerate(properties):
                                if z.isdigit():
                                    properties[n] = int(z)
                            
                            if i[0] == 'Branch':
                                branch = class_(*properties)
                            elif i[0] == 'Director':
                                director = class_(branch, *properties)
                            elif i[0] == 'Employee':                            
                                employee = class_(director, *properties)
                            elif i[0] == 'Customer':                            
                                customer = class_(director, employee, *properties[0:-1])
                                account = customer.add_account()
                                account.balance = properties[-1]
                            elif i[0] == 'Credit':
                                credit = class_(*properties[0:-1])
                                start_data = (int(n) for n in properties[-1].split('-'))
                                credit.start_date = datetime.date(*start_data)
                                account.assign_credit_amount_to_account(credit)
                            elif i[0] == 'AccountLimit':
                                account_limit = class_(*properties)
                                account.assign_credit_amount_to_account(account_limit)
    
    @staticmethod
    def save_data():
        with open('static/data.csv', 'w', encoding='utf16') as f:
            writer = csv.writer(f)
            for branch in Branch.all_branches:
                writer.writerow([branch.__class__.__name__ , branch.town])
                writer.writerow([branch.director.__class__.__name__, branch.director.name, branch.director.surname, branch.director.birth])
                for employee in branch.director.employees:
                    writer.writerow([employee.__class__.__name__, employee.earnings, employee.name, employee.surname, employee.birth])
                    for customer in employee.customers:
                        writer.writerow([customer.__class__.__name__, customer.earnings, customer.name, customer.surname, customer.birth, customer.account.balance])
                        if customer.account.products:
                            for product in customer.account.products:
                                if isinstance(product, Product):
                                    writer.writerow([product.__class__.__name__, product.amount_of_credit, product.period, product.start_date])
                                else:
                                    writer.writerow([product.__class__.__name__, product.amount_of_credit, product.amount_of_credit_used])
                                    

    @staticmethod
    def save_password():
        password = "123"
        password = sha256_crypt.encrypt(password)
        with open('static/login.csv', 'w', encoding='utf16') as f:
            writer = csv.writer(f)
            for branch in Branch.all_branches:
                writer.writerow([branch.director.name, password])
                for employee in branch.director.employees:
                    writer.writerow([employee.name, password])
                    for customer in employee.customers:
                        writer.writerow([customer.name, password])

    @staticmethod
    def save_password_new_person(name, password):
        password = sha256_crypt.encrypt(password)
        with open('static/login.csv', 'a', encoding='utf16') as f:
            writer = csv.writer(f)                
            writer.writerow([name, password])

    @staticmethod
    def load_password():
        passwords = {}
        with open('static/login.csv', 'r', encoding='utf16') as f:
            reader = csv.reader(f)
            for person in reader:
                if person:
                    passwords[person[0]] = person[1]
        return passwords