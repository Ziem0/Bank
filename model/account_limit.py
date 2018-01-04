from model.product_flex import ProductFlex

class AccountLimit(ProductFlex):

    PERCENT = 0.01 

    def __init__(self, *args):
        super().__init__(*args)
        
