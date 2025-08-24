class Employee:
    def __init__(self, name, alias, salary):
        self.name = name
        self.alias = alias
        self.salary = salary

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    # useful only to print single instance
    def __str__(self):
        return "Employee(name={}, alias={}, salary={})".format(self.name, self.alias, self.salary)

    # useful to print both collection of instance and single instance
    def __repr__(self):
        return self.__str__()