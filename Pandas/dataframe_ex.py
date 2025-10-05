import pandas as pd

nolan_movies = pd.DataFrame(
    {"Director": ["Nolan", "Nolan", "Nolan"],
     "Movies": ["Interstellar", "Inception", "Tenet"]})
fincher_movies = pd.DataFrame(
    {"Director": ["Fincher", "Fincher", "Fincher"],
     "Movies": ["Fight Club", "Zodiac", "Gone Girl"]})
taranto_movies = pd.DataFrame(
    {"Director": ["Quentin Tarantino", "Quentin Tarantino", "Quentin Tarantino"],
     "Movies": ["Inglourious Basterds", "Once Upon a Time in Hollywood", "Kill Bill"]})

df_combined = pd.concat([nolan_movies, fincher_movies, taranto_movies])  # add row
df_combined.reset_index(drop=True, inplace=True)
rating_df = pd.DataFrame({"Rating": [10, 10, 10]})
df_combined = pd.concat([df_combined, rating_df], axis=1)  # add column
# df_combined["Rating"] = 10 all the rows should have same value then this approach is fine
print(len(df_combined))
print(df_combined)