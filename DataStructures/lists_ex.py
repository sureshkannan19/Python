movies = ["Interstellar", "Inception", "Tenet", "Batman Begins", "The Dark Knight", "The Dark Knight Rises",
          "The Prestige",
          "Jo Jo Rabbit", "1917", "Inglorious Bastards", "Django Unchained", "Kill Bill",
          "Seven", "F1", "Fight Club",
          "Terminal", "Captain Phillips", "Forest Gump", "The Green Mile", "Good will hunting",
          "The Shawshank Redemption", "Dead Poets Society",
          "Leon: The Professional", "John Wick", "Mad max",
          "Terminator", "X-men: the last stand", "X-men: the first class", "The Truman show", "Avengers", "Iron man"]

movies.remove("Iron man")  # removes last element by value and returns None
print(movies[-1])  # access last element
removed_element = movies.pop(-1)  # removes last element by index and returns the value
print(removed_element)

empty_list = []
try:
    print(empty_list.pop())  # if list is empty throws IndexError
except IndexError as e:
    print(e)
empty_list.append(1)
empty_list.append(2)
print(empty_list.pop())  # pop without index, pops the last added element

try:
    movies.remove("Avengers")  # if element not present ValueError is thrown
except ValueError as e:
    print(e)

movies.insert(8, 'The Bird man')  # Insert value at given index
print(movies[8])  # access via index

print(f"Before adding to the list: {len(movies)}")  # to find length of the list
movies.extend(
    ["Batman vs Superman: Dawn of Justice", "Justice League", "Aquaman", "Man of Steel"])  # extends another list
print(f"After adding to the list: {len(movies)}")

print(movies[-1])
movies[-1] = "Superman: Man of Steel"  # mutable hence value can be changed
print(movies[-1])

print(movies.count("Tenet"))  # counts no of occurrence
print(movies.index("F1"))  # returns the index of first occurrence of the value

try:
    print(movies.index("F11"))  # returns ValueError if element not found
except ValueError as e:
    print(e)

# slices creates new array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1:8:2])  # start index, stop index (exclusive), and step (i.e 2 steps from current place)

print(numbers[1:8])  # from 1st index to 8th index(exclusive)
print(numbers[:8])  # from 0th index to 8th index(exclusive)
print(numbers[1:])  # from 1st index till end
print(numbers[:])  # creates new array with all elements
print(numbers[-3:])  # from 3rd last element to the end of the list

numbers_copy = numbers.copy()
print(numbers_copy is numbers)  # False
print(numbers_copy == numbers)  # True
numbers_copy.pop()
print(numbers_copy == numbers)  # False

if "F1" in movies:
    print("Value present")

print([i for i in range(5)])  # [0, 1, 2, 3, 4]

numbers.sort()
print("In-place sorting", numbers)  # in-place sorted
numbers.sort(reverse=True)
print("In-place reverse sorting", numbers)  # in-place reverse sorted

print(sorted(numbers_copy))  # produces new sorted array
print(sorted(numbers_copy, reverse=True))  # produces new reverse sorted array

movies.reverse()
# print(movies)

mix_array = [1, "xsa"]
# mix_array.sort() # TypeError
# print(sorted(mix_array)) # TypeError

print([1, 2] * 3)  # [1, 2, 1, 2, 1, 2] # multiplies the same list thrice
print([1, 2] + [1])  # [1, 2, 1] # adds two list

print(" & ".join(["Apple", "Banana"]))

print(max(numbers))
print(min(numbers))
print(sum(numbers))

list_of_list = [
    [1, "SK", 27, "Single"],
    [2, "Suresh K", 28, "Parent"],
    [3, "Suresh Babu K", 55, "Grand Parent"]
]

dup_list = list_of_list.copy()
print(f"Is same instance {dup_list[0] is list_of_list[0]}")
dup_list[0][1] = "Jon Snow"
print(f"Is same instance {dup_list[0][1] == list_of_list[0][1]}")

for id, name, *details in list_of_list:  # Un packing
    print(id, name, details)

for i, movie in enumerate(movies):
    if i == 2:
        movies.insert(2, "Momento")  # if break not added goes to infinite loop
        break;

print(movies)

import timeit

large_list = list(range(100000))


def access_element():
    _ = large_list[50000]


def append_element():
    large_list.append("new_element")


def remove_element():
    large_list.remove("new_element")


def insert_element():
    large_list.insert(50000, "inserted_element")


access_time = timeit.timeit(access_element, number=1000)
append_time = timeit.timeit(append_element, number=1000)
remove_time = timeit.timeit(remove_element, number=1000)
insert_time = timeit.timeit(insert_element, number=1000)

print(f"Access time: {access_time} seconds")
print(f"Append time: {append_time} seconds")
print(f"Remove time: {remove_time} seconds")
print(f"Insert time: {insert_time} seconds")

numbers.clear() # clears all the value