import pandas as pd
import os

folder_original = os.path.expanduser("~/PycharmProjects/PythonProject/resources/quotes.json")
df_fron_json = pd.read_json(folder_original)
print(df_fron_json)