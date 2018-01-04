from ui.ui import UI

class CustomerUI(UI):
    
    menu = ['Check account balance', 'Cash in ', 'Cash out', 'Monthly repayment', 'Repaid credit', 'Use account limit', 'Exit']
    title1 = '\n\nCustomer menu:\n\n'
    title2 = '\n\nInsufficient funds!\n\n'
    title3 = '\n\nAdd product\n\n'
    title4 = '\n\nRepaid credit\n\n'
    title5 = '\n\nCustomer\'s products: \n\n'
    title6 = '\n\nThis value is higher than Your account limit. Your max limit is: '

    @staticmethod
    def cash_in_out_inputs():
        amount = ''
        while not isinstance(amount, int):
            try:
                amount = int(input('\nType amount: '))
            except ValueError:
                print('Only numbers!')
        return amount
