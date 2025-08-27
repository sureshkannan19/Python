class Employee:

    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee's salary is {self.salary}"

    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)}, {self.salary})"

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class SlotsInspectMixin:
    __slots__ = ()
    def has_slots(self):
        return hasattr(self, "__slots__")

class Developer(SlotsInspectMixin, Employee):
    __slots__ = ("tech_stack")
    def __init__(self, name, age, salary, tech_stack):
        super().__init__(name, age, salary)
        self.tech_stack = tech_stack

    def increase_salary(self, percent, bonus = 0):
        super().increase_salary(percent)
        self.salary += bonus

    def has_slots(self):
        return hasattr(self, "__slots__")

dev = Developer("SK-Dev", 27, 100, 'Java,Spring,Python')
print(dev)
print(dev.has_slots()) # True
print(Developer.__mro__) # Method Resolution Order # (<class '__main__.Developer'>, <class '__main__.SlotsInspectMixin'>, <class '__main__.Employee'>, <class 'object'>)
