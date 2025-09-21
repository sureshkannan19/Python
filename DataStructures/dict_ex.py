from operator import itemgetter

square_dict = {x: x * x for x in range(6)}
print(square_dict)


square_dict = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
inverted_dict = {v : k for k, v, in square_dict.items()}
print(inverted_dict)

director_movies = {"Nolan" : ["Interstellar", "Inception"]}
shallow_copy_dir_mov = director_movies.copy()
print(shallow_copy_dir_mov == director_movies)
shallow_copy_dir_mov["Nolan"].append("Tenet") # ["Interstellar", "Inception", "Tenet"]
print(shallow_copy_dir_mov["Nolan"])
print(director_movies["Nolan"])

import copy

deep_copy_dir_mov = copy.deepcopy(director_movies)
deep_copy_dir_mov["Nolan"].append("The Prestige") # ["Interstellar", "Inception", "Tenet", "The Prestige"]
print(deep_copy_dir_mov == director_movies)
print(deep_copy_dir_mov["Nolan"])
print(director_movies["Nolan"])


group_by_first_letter = {}
for movie in director_movies["Nolan"]:
    group_by_first_letter.setdefault(movie[0], []).append(movie) # equivalent to computeIfAbsent

print(group_by_first_letter)

print(group_by_first_letter.items()) # viewed as tuple

sorted_by_key_dict = dict(sorted(group_by_first_letter.items(), reverse=True)) # sort by key
print(sorted_by_key_dict) # view

sorted_by_value_dict = dict(sorted(group_by_first_letter.items(), key=lambda item: len(item[1]))) # sort by key
print(sorted_by_value_dict) # view


series = {"Eric Kripke": ["Supernatural", "The Boyz"]}
all_shows =  director_movies | series # merge operator to add both dicts, if same key exist, then last added dict key - value is retained
print(all_shows)


nums1 = [1,2,]
try:
    dict_chk = {nums1: []}   # TypeError: unhashable type: 'list'
except TypeError as e:
    print(e)
