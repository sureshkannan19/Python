class Employee:

    __slots__ = ("name", "age", "__salary") # tells python that only these are the properties of the class so that at runtime we dont/cant create new properties

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError('Salary cannot be negative')
        self.__salary = salary

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee's salary is {self.salary}"

    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)}, {self.salary})"

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class Developer(Employee):
    __slots__ = ("tech_stack")
    def __init__(self, name, age, salary, tech_stack):
        super().__init__(name, age, salary)
        self.tech_stack = tech_stack

    def increase_salary(self, percent, bonus = 0):
        super().increase_salary(percent)
        self.salary += bonus

class Tester(Employee):
    pass

dev = Developer("SK-Dev", 27, 100, 'Java,Spring,Python')
try:
    dev.new_property = 1
except AttributeError as e:
    print('Dynamic property creation is not allowed, because slots replaced dict')

dev.increase_salary(30, 20)
print(dev)

test = Tester("SK-Test", 27, 100)
test.increase_salary(30)
print(test)