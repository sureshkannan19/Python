
file_location = "../resources/FavouriteQuotes.txt"

def find_favourite_quotes():
    look_up_word = input("Keyword you were looking for?\n")
    found = False
    try:
        with open(file_location) as file: # C:/Users/SureshBabu/PycharmProjects/PythonProject/resources/FavouriteQuotes.txt -> both works
            for line in file:
                if look_up_word in line:
                    print(line)
                    found = True
    except FileNotFoundError or Exception as e:
        print("Error occurred while trying to open the file:", e)
        return
    if not found:
        print("Keyword not found")

def add_favourite_quotes():
    favorite_quote = input("Your favourite quote?\n")
    source = input("and it's source?\n")
    with open(file_location, "a") as file: # C:/Users/SureshBabu/PycharmProjects/PythonProject/resources/FavouriteQuotes.txt -> both works
        file.write("\n" +favorite_quote + " - "+ source)

def main():
    choice = input("Do you want to find(F) or add(A) quotes?\n")
    if choice.capitalize() == "F": find_favourite_quotes()
    else: add_favourite_quotes()

main()