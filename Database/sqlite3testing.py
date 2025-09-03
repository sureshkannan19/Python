import sqlite3
import click

from dataclasses import dataclass


@dataclass
class Quotes:
    id: int
    quote: str
    source: str


def dict_factory(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


@click.group()
def cli():
    pass


@cli.command()
@click.option("--source", default="Lucifer")
def get_quotes(source):
    print("Given source:", source)
    database = sqlite3.connect("shows.db")
    database.row_factory = dict_factory
    cursor = database.cursor()
    cursor.execute("select * from quotes where source =?", (source,))
    print([Quotes(**q) for q in cursor.fetchall()])


if __name__ == "__main__":
    cli()
