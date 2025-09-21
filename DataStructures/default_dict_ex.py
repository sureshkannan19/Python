from collections import defaultdict

dd = defaultdict(int)
numbers = [1, 2, 3, 4, 2, 5, 6, 7, 8, 2, 3, 4, 5, 1, 2, 3, 8, 9, 6]
for number in numbers:
    dd[number] += 1
print(dd)

dd_list = defaultdict(list)
foods = ['apple', 'banana', 'beetroot', 'grapes', 'apricot']
for food in foods:
    dd_list[food[0]].append(food)
print(dd_list)


def default_factory(fromSource):
    print(f'default factory {fromSource}')
    return []

dd_list_factory = defaultdict(lambda : default_factory('from defaultdict'), {'a': []})
std_dict = {}
foods = ['apple', 'banana', 'beetroot', 'grapes', 'apricot']
for food in foods:
    dd_list_factory[food[0]].append(food)
    std_dict.setdefault(food[0], default_factory('from std dict')).append(food)
print(dd_list_factory)
