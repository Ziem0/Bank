from model.product import Product
import math

class Credit(Product):
    
    PERCENT = 0.08 

    def __init__(self, *args):
        super().__init__(*args)
        