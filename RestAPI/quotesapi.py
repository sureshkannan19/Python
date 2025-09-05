import uvicorn

from fastapi import FastAPI

from schemas import save_quotes_to_json
from schemas import get_quotes_from_json, QuotesInput, QuotesOutput

app = FastAPI(title="Quotes")


@app.get("/quotes")
def get_quotes(source: str | None = None) -> list[QuotesOutput]:
    return get_quotes_from_json(source)


@app.post("/quotes")
def save_quotes(quote: QuotesInput) -> list[QuotesOutput]:
    all_quotes = get_quotes_from_json(None)
    all_quotes.append(QuotesOutput(id=len(all_quotes) + 1, quote=quote.quote, source=quote.source))
    return save_quotes_to_json(all_quotes)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
