import json
import os
from typing import List

from pydantic import BaseModel

from RestAPI.entities import Quotes, Shows, Characters

filepath = os.path.expanduser("~/PycharmProjects/PythonProject/resources/quotes.json")


class QuotesInput(BaseModel):
    quote: str
    source: str | None = "RANDOM"
    model_config = {
        "json_schema_extra": {
            "examples": [{
                "quote": "What do you truly desire?",
                "source": "Lucifer",
            }]
        }
    }


class QuotesOutput(QuotesInput):
    id: int

    @classmethod
    def entity_to_model(cls, quote: Quotes):
        return QuotesOutput(id=quote.id, quote=quote.quote, source=quote.source)


def get_quotes_from_json(source):
    try:
        with open(filepath) as f:
            return [QuotesOutput.model_validate(obj) for obj in json.load(f) if source is None or obj['source'] == source]
    except FileNotFoundError:
        print("File not found", filepath)


def save_quotes_to_json(quotes: list[QuotesOutput]):
    try:
        with open(filepath, "w") as f:
            json.dump([q.model_dump() for q in quotes], f, indent=4)
    except FileNotFoundError:
        print("File not found", filepath)
    return quotes


class CharactersIn(BaseModel):
    ch_name: str
    role: str
    model_config = {
        "json_schema_extra": {
            "examples": [{
                "ch_name": "Lucifer",
                "role": "Punisher",
                "show_id": 1,
            }]
        }
    }


class CharactersOut(CharactersIn):
    ch_id: int
    show_id: int

    @classmethod
    def entities_to_models(cls, chs: List[Characters]):
        return [CharactersOut(ch_id=ch.ch_id, show_id=ch.show_id, ch_name=ch.ch_name, role=ch.role) for ch in chs]

    @classmethod
    def entity_to_model(cls, ch: Characters):
        return CharactersOut(ch_id=ch.ch_id, show_id=ch.show_id, ch_name=ch.ch_name, role=ch.role)


class ShowsIn(BaseModel):
    genre: str | None = "ALL"
    show_name: str
    characters: list[CharactersIn] | None = []
    model_config = {
        "json_schema_extra": {
            "examples": [{
                "show_name": "Lucifer",
                "genre": "Sci-fi,Action,Romance,Comedy,Mythology",
                "characters": [
                    {
                        "ch_name": "Lucifier",
                        "role": "Punisher",
                    }
                ]
            }]
        }
    }


class ShowsOut(ShowsIn):
    show_id: int

    @classmethod
    def entity_to_model(cls, show: Shows):
        return ShowsOut(show_id=show.show_id, show_name=show.show_name, genre=show.genre,
                        characters=[CharactersOut.entity_to_model(ch) for ch in show.characters])
