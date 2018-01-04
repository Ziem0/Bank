from model.person import Person

class Director(Person):

    all_directors = []

    def __init__(self, branch, *args):
        self.branch = branch
        super().__init__(*args)
        self.employees = []
        self.customers = []

        self.branch.assign_director(self)
        Director.all_directors.append(self)

    def add_employee(self, employee):
        self.employees.append(employee)
        return self.employees[-1]

    def add_customer(self, customer):
        self.customers.append(customer)
        return self.customers[-1]

    def __str__(self):
        data = "name:{}\nsurname:{}\nbranch:{}".format(self.name, self.surname, self.branch.create_unique())
        out = ''
        for employee in self.employees:
            out += str(employee)
        return "{}\n{}".format(data, out)