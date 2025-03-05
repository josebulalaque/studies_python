from myemployee import Employee, SalaryEmployee, HourlyEmployee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees: ')
        for i in self.employees:
            print(i.first, i.last)
        print('-----------------------------')


def main():
    my_company = Company()

    emp1 = SalaryEmployee('Pepito', 'Manaloto', 80000)
    my_company.add_employee(emp1)

    emp2 = HourlyEmployee('Pepe', 'Smith', 25, 50)
    my_company.add_employee(emp2)

    emp3 = HourlyEmployee('Andrew', 'Worldwide', 40, 15)
    my_company.add_employee(emp3)

    my_company.display_employees()
    print(emp3.fullname())
    print(emp3.calculate_paycheck())

main()