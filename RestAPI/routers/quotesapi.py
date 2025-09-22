from typing import Annotated
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from RestAPI.dbconfig import get_session
from RestAPI.entities import Quotes
from fastapi import Depends, APIRouter

from RestAPI.schemas import save_quotes_to_json
from RestAPI.schemas import get_quotes_from_json, QuotesInput, QuotesOutput

router = APIRouter(prefix="/quotes")


@router.get("/json")
def get_quotes(source: str | None = None) -> list[QuotesOutput]:
    return get_quotes_from_json(source)


@router.post("/json")
def save_quotes(quote: QuotesInput) -> list[QuotesOutput]:
    all_quotes = get_quotes_from_json(None)
    all_quotes.append(QuotesOutput(id=len(all_quotes) + 1, quote=quote.quote, source=quote.source))
    return save_quotes_to_json(all_quotes)


@router.get("/db")
async def get_quotes(session: Annotated[AsyncSession, Depends(get_session)], source: str | None = None) -> list[
    QuotesOutput]:
    stmt = select(Quotes)
    if source is not None:
        stmt = stmt.where(Quotes.source == source)
    result = await session.execute(stmt)
    return [QuotesOutput.entity_to_model(q) for q in result.scalars().all()]


@router.post("/db")
async def save_quotes(session: Annotated[AsyncSession, Depends(get_session)],
                quote_in: QuotesInput) -> list[QuotesOutput]:
    quotes_entity = Quotes(quote=quote_in.quote, source=quote_in.source)
    session.add(quotes_entity)
    await session.commit()
    await session.refresh(quotes_entity)
    stmt = select(Quotes)
    result = await session.execute(stmt)
    return [QuotesOutput.entity_to_model(q) for q in result.scalars().all()]


@router.delete("/json/{quote_id}", status_code=204)
def save_quotes(quote_id: int):
    all_quotes = get_quotes_from_json(None)
    save_quotes_to_json([q for q in all_quotes if q.id != quote_id])
