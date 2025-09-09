from typing import Annotated
from sqlalchemy import select
from sqlalchemy.orm import Session
from RestAPI.dbconfig import get_session
from RestAPI.entities import Shows, Characters
from fastapi import Depends, APIRouter
from RestAPI.schemas import ShowsOut, ShowsIn
show_router = APIRouter()

@show_router.get("/shows")
async def get_shows(session: Annotated[Session, Depends(get_session)],
                    show_name: str | None = None) -> list[ShowsOut]:
    stmt = select(Shows)
    if show_name is not None:
        stmt = stmt.where(Shows.show_name == show_name)
    return [ShowsOut.entity_to_model(q) for q in session.execute(stmt).scalars().all()]


@show_router.post("/shows")
async def upsert_shows(session: Annotated[Session, Depends(get_session)], show: ShowsIn) -> ShowsOut:
    show_entity = Shows(show_name=show.show_name, genre=show.genre)
    show_entity.characters.extend(
        [Characters(ch_name=ch.ch_name, role=ch.role, show_id=show_entity.show_id, shows=show_entity) for ch in
         show.characters])
    session.add(show_entity)
    session.commit()
    session.refresh(show_entity)
    return ShowsOut.entity_to_model(show_entity)
