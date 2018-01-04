class Person:
    '''
    This class serves as a template for suitable people
    '''

    def __init__(self, name, surname, birth):
        self.name = name
        self.surname = surname
        self.birth = birth
        
        if not isinstance(self.birth, int):
            raise ValueError

    def calculate_age(self):
        age = (datetime.date.today().year - datetime.date(self.birth,1,1).year)
        return age

    