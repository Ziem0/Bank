from model.product_flex import ProductFlex

class CardCredit(ProductFlex):
    
    PERCENT = 0.03

    def __init__(self, *args):
        super().__init__(*args)
    