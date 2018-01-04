from model.person import Person

class Employee(Person):
    
    all_employees = []

    def __init__(self, director, earnings, *args):
        self.director = director
        self.earnings = earnings
        super().__init__(*args)
        self.customers = []

        self.director.add_employee(self)
        Employee.all_employees.append(self)

    def add_customer(self, customer):
        self.customers.append(customer)
        return self.customers[-1]

    def calculate_commission(self):
        if self.customers:
            commission = (len(self.customers)/10) * self.earnings
            return commission

    def __str__(self):
        data =  "name:{}\nsurname:{}\nbranch:{}\n\nCustomers:\n".format(self.name, self.surname, self.director.branch.create_unique())
        out = ""
        for customer in self.customers:
            out += str(customer)
        return "{}\n{}".format(data, out)
        

