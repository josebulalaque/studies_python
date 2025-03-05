class Employee:
    def __init__(self, fname, lname):
        self.first = fname
        self.last = lname
        self.email = fname + '.' + lname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname,)
        self.pay = salary

    def calculate_paycheck(self):
        return self.pay/52

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)    
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.weekly_hours*self.hourly_rate
# employee1 = Employee("Juan", "Dela Cruz", 50000)



# print(employee1.fullname())
# print(employee1.calculate_paycheck())

