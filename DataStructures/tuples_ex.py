def min_max(input_list):
    return min(input_list), max(input_list)  # considered as tuple hence able to unpack at line 6

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

min_val, max_val = min_max(numbers)
print(f'Min value: {min_val}, Max value: {max_val}')


def entitled_users(*users):
    print(users)  #


entitled_users('user1', 'user2')

tuple_example = (1, [2, 3], 4)
tuple_example[1].append(5) # tuple is immutable but the internal value can be change if is mutable( list or object)
print(tuple_example)