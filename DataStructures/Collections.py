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
c_list = [5 * x if x%5 == 0 else x for x in  range(26)]
print(c_list)

# Generated Expression
gen = (x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


print(type((1 , 2, 3)))
print(type(gen))
print(list(gen))

print(list(enumerate(['a', 'b', 'c'], 0)))

array = [1, 2, 3, 4]
array.extend([5, 6])
print(array)