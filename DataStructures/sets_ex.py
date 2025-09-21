set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {1, 2, 3, 4, 5}
set4 = (6, 7, 8, 9, 10)

print("Union elements: ", set1 | set2)

print("Common elements: ", set1 & set2)
print("Common elements: ", set1.intersection(set2))  # accepts any iterable as second argument

print("Difference: ", set1 - set2)
print("Difference: ", set1.difference(set2))  # accepts any iterable as second argument

print("Symmetric difference: ", set1 ^ set2)  # elements does not present in both list
print("Symmetric difference: ", set1.symmetric_difference(set2))  # accepts any iterable as second argument

print(set1.issubset(set3)) # all elements in set 1 present in set 3
print(set3.issuperset(set1)) # all elements in set 1 present in set 3
print(set3.isdisjoint(set4)) # no elements match

immutable_set = frozenset((1, 2, 3, 4, 5))
try:
    immutable_set.add(4)
except AttributeError as e:
    print(e)




class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        if self is other:
            return True
        return self.name == other.name and self.emp_id == other.emp_id

    def __hash__(self):
        return hash((self.emp_id, self.name))

    def __repr__(self):
        return f'Employee({self.emp_id}, {self.name}, {self.salary})'


emp1 = Employee(1, 'A', 100)
emp2 = Employee(2, 'B', 200)
emp3 = Employee(1, 'A', 300)

unique_list = {emp1, emp2, emp3}
print(unique_list)
