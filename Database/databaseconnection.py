import psycopg2
import psycopg2.extras
from dataclasses import dataclass

connection = psycopg2.connect(host="localhost",database="pydb",user="sk_user",password="adminsk", port="5432")

@dataclass(slots=True)
class Quotes:
    id: int
    quote: str
    source: str

def add_quotes():
    cursor = connection.cursor()
    quote = input("What's your favourite quote?\n")
    source = input("What the source?\n")
    data = [(quote, source)]
    psycopg2.extras.execute_values(cursor, "INSERT INTO shows.quotes (quote, source) VALUES %s", data)
    connection.commit()
    cursor.close()
    connection.close()

# add_quotes()

dict_cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
dict_cursor.execute("select * from shows.quotes")
quotes = [Quotes(**row) for row in dict_cursor.fetchall()]
print(quotes)
dict_cursor.close()
connection.close()
