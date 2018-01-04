import datetime
import math
from abc import ABC, abstractmethod


class Product(ABC):
    
    all_products = {'Credit':[0,0], 'CardCredit':[0,0], 'AccountLimit':[0,0]}

    def __init__(self, amount_of_credit, period):
        self.amount_of_credit = amount_of_credit
        self.period = period
        self.start_date = datetime.date.today()

        for product, properties in Product.all_products.items():
            if product == self.__class__.__name__:
                properties[0] += 1
                properties[1] += self.calculate_interest() 

    def set_date_repayment(self):
        self.end_credit = self.start_date
        self.end_credit += datetime.timedelta(self.period * 30)
        return self.end_credit

    def automatical_monthly_repayment(self):
        self.set_date_repayment()
        today = datetime.date.today()
        difference = (self.end_credit - today).days
        if today.day == 1 and difference >= 0:
            cash_to_pay = self.calculate_monthly_repayment()
            return cash_to_pay
        else:
            return 0

    def calculate_monthly_repayment(self):
        monthly_repayment = (self.calculate_interest() / self.period) + (self.amount_of_credit / self.period)
        return math.ceil(monthly_repayment)
    
    def calculate_interest(self):
        interest = self.amount_of_credit * (self.period * self.__class__.PERCENT)        
        return math.ceil(interest)
