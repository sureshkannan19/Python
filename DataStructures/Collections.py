try:
    s = {[1,2,3], [4,5,6]}
except Exception as e:
    print("Error occurred while storing in set:", e.__str__())


def add_to_list(value, list=None):
    if list is None:
        list = []
    list.append(value)
    return list

print(add_to_list(1))
print(add_to_list(2))

#comprehensive way to populate data structures
c_list = [5 * x for x in range(26) if x%5 == 0]
print(c_list)

# Generated Expression
gen = (5 * x for x in range(26) if x%5 == 0)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


print(type((1 , 2, 3)))