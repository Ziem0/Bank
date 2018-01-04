from ui.ui import UI

class EmployeeUI(UI):
    
    menu = ['Show all customers', 'Add new customer', 'Customer menu', 'Show my commission+earnings', 'Exit']
    menu1 = ['Add account', 'Add product', 'Return']
    menu2 = ['Credit', 'AccountLimit']
    title1 = '\n\nEmployee menu:\n\n'
    title2 = '\n\nCustomer menu:\n\n'
    title3 = '\n\nYour customer(s):\n\n'
    title4 = '\n\nAdd new product: \n\n'

    @staticmethod
    def new_customer_inputs():
        surname = input('your surname: ')
        birth = int(input('birth year: '))
        earnings = int(input('your earnings: '))
        return surname, birth, earnings

    @staticmethod
    def new_credit_inputs():
        amount = int(input('Type amount of credit: '))
        period = int(input('Specify period: '))
        return amount, period

    @staticmethod
    def new_creditflex_inputs():
        amount = int(input('Type amount of credit: '))
        return amount        