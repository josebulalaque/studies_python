class Employee:
    def __init__(self, fname, lname, salary):
        self.first = fname
        self.last = lname
        self.pay = salary
        self.email = fname + '.' + lname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def calculate_paycheck(self):
        return self.pay/52
    

# employee1 = Employee("Juan", "Dela Cruz", 50000)

# print(employee1.fullname())
# print(employee1.calculate_paycheck())

