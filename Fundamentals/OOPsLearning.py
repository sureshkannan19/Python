from employee import *


class Company:

    def __init__(self, company_name):
        self.employees = []
        self.company_name = company_name

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        print(self.employees)

    def purpose(self):
        return "Nothing chill and get paid guyz"


class HunterCorp(Company):
    def __init__(self, name):
        super().__init__(name)

    def purpose(self):
        return "Purpose of HunterCorp: Hunt evil with supernatural abilities"


c = HunterCorp("HunterCorp")
e = Employee("Lucifer", "The Devil", 200000)
c.add_employee(e)
e = Employee("Castiel", "Angel", 200000)
c.add_employee(e)
e = Employee("Dean Winchester", "Hunter", 200000)
c.add_employee(e)
c.print_employees()
print(c.purpose())
