quote = input("What's your favourite quote:")
print(quote)

for i in range(0, 7, 2):
    print(i)
    break

movies_i_like = ["Inception", "Leo"]
for i in movies_i_like:
    print("Inside for loop:", i)

movies_i_like.remove("Leo")

print(movies_i_like)

if movies_i_like.__contains__("Inception"):
    print("Present")

my_dict = {"Nolan": ["Inception", "Interstellar", "Batman Triology", "Tenet"], "Alejandro Inaritu": "The Bird Man"}

print(my_dict.get("Nope")) # None
for k in my_dict:  #  Just Keys
    pass # can be used if empty loop or conditions(if -elif) or empty methods
    print("Key:", k)

for k, v in my_dict.items():
    print("Key:", k, "Value:", v)  # False

try:
    movies_i_like[1]
except IndexError:
    raise Exception("Leo doesn't exist")
finally:
    print("Inside finally")