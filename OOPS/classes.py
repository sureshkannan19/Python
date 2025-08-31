from datetime import date

class Employee:

    minimum_wage = 1000 # class property

    @classmethod
    def compute_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Company is bankrupt")
        cls.minimum_wage = new_wage

    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year
        return cls(name, age, cls.minimum_wage)

    # _single_underscore → “protected” (internal use, but accessible).
    # __double_underscore → name mangling
    # In Python, Encapsulation is done by convention, not by compiler enforcement like in Java
    def __init__(self, name, age, salary):
        self.__salary = None
        self.name = name
        self.age = age
        self.salary = salary # calling computed property
        self.minimum_wage = 2000 # instance property

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError('Salary cannot be negative')
        self.__salary = salary

    @property
    def annual_salary(self):
        return self.__salary * 12

    def increase_salary(self, increase_by):
        self.__salary += self.__salary * increase_by
        return self.__salary

    # Non-tech user-friendly info
    # print(instance) executes below functions in order, if below methods are not overridden
    # 1. __str__ method
    # 2. __repr__ method
    # 3. __repr__ in object class which prints hexadecimal memory address
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee's salary is {self.__salary}"

    # Developer friendly
    # it also executed on printing collections of a class
    # print([e1, e2])
    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)}, {self.__salary})"

e = Employee("SK", 27, 1000)
try:
    print(e.__salary)
    # __salary 'Name Mangling', makes accessing property harder but still it's accessible through class name '_Employee__salary'
except AttributeError as ex:
    print(ex)
    print("Access Salary via getter:", e.salary)

# print(e.__dict__)

e.salary = 2000  # Employee.change_salary(e, 100)
print("Updated salary:", e.salary)
print("Annual salary:", e.annual_salary)

print(e) # uses __str__   --->  SK is 27 years old. Employee's salary is 2000
print(repr(e))
Employee.__dict__["increase_salary"](e, 10) # classes are object too
print("Updated salary:", e.salary)

print("Minimum salary:", e.minimum_wage) # instance value
print("Minimum salary:", Employee.minimum_wage) # class value

e1 = Employee.new_employee("Dean", date(1998, 6, 19))
print(e1)

def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, a=10, b=20)
# args: (1, 2, 3)
# kwargs: {'a': 10, 'b': 20}