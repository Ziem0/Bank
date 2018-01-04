from ui.ui import UI

class DirectorUI(UI):
    
    menu = ['Show all employees', 'Show all customers', 'Add new employee', 'Show all interest', 'Show all deposit', 'Exit']
    title1 = '\n\nDirector menu:\n\n' 
    title2 = '\n\nYour employees:\n\n'
    title3 = '\n\nBranch customers\n\n'

    @staticmethod
    def new_employee_inputs():
        surname = input('surname: ')
        birth = int(input('birth year: '))
        earnings = int(input('earnings: '))
        return surname, birth, earnings