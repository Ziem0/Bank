import datetime
import math
from model.product import Product
from abc import ABC, abstractmethod

class ProductFlex(ABC):
    
    def __init__(self, amount_of_credit, amount_of_credit_used=0):
        self.amount_of_credit = amount_of_credit
        self.amount_of_credit_used = amount_of_credit_used
        self.screen = "+ Account Limit: {}\n+ Used credit: {}".format(self.amount_of_credit, self.amount_of_credit_used)

        for product, properties in Product.all_products.items():
            if product == self.__class__.__name__:
                properties[0] += 1

    def set_date_repayment(self):
        self.start_credit = datetime.date.today()
        end_credit = datetime.date.today()
        self.period = (end_credit - self.start_credit).days
        return self.period

    def calculate_repayment(self):
        credit_repayment = self.calculate_interest() + self.amount_of_credit_used

        for product, properties in Product.all_products.items():
            if product == self.__class__.__name__:
                properties[1] += self.calculate_interest() 

        self.amount_of_credit_used = 0
        return math.ceil(credit_repayment)

    def calculate_interest(self):
        interest = self.amount_of_credit_used * (self.period * self.__class__.PERCENT)        
        return math.ceil(interest)

