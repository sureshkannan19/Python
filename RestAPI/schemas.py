import json
import os

from pydantic import BaseModel

filepath = os.path.expanduser("~/PycharmProjects/PythonProject/resources/quotes.json")


class QuotesInput(BaseModel):
    quote: str
    source: str | None = "RANDOM"
    model_config = {
        "json_schema_extra" :{
            "examples": [{
                "quote": "What do you truly desire?",
                "source": "Lucifer",
            }]
        }
    }

class QuotesOutput(QuotesInput):
    id: int


def get_quotes_from_json(source):
    try:
        with open(filepath) as f:
            return [QuotesOutput.model_validate(obj) if source is None else obj['source'] == source for obj in json.load(f)]
    except FileNotFoundError:
        print("File not found", filepath)


def save_quotes_to_json(quotes: list[QuotesOutput]):
    try:
        with open(filepath, "w") as f:
            json.dump([q.model_dump() for q in quotes], f, indent=4)
    except FileNotFoundError:
        print("File not found", filepath)
    return quotes
