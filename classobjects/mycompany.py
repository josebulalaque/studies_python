from myemployee import Employee

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

    emp1 = Employee('Pepito', 'Manaloto', 80000)
    my_company.add_employee(emp1)

    emp2 = Employee('Pepe', 'Smith', 1000000)
    my_company.add_employee(emp2)

    emp3 = Employee('Andrew', 'Worldwide', 80)
    my_company.add_employee(emp3)

    my_company.display_employees()


main()