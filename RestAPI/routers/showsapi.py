import os.path
from typing import Annotated

from RestAPI.dbconfig import get_session
from RestAPI.entities import Shows, Characters
from RestAPI.exceptions.exceptions import ShowNotFoundException
from RestAPI.schemas import ShowsOut, ShowsIn, CharactersOut
from fastapi import Depends, APIRouter, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/shows")



@router.get("/")
async def get_shows(session: Annotated[AsyncSession, Depends(get_session)],
                    token: Annotated[str | None, Header()] = None,
                    show_name: str | None = None) -> list[ShowsOut]:
    print(f"Token is {token}")
    stmt = select(Shows)
    if show_name is not None:
        stmt = stmt.where(Shows.show_name == show_name)
    result = await session.execute(stmt)
    if not result and show_name is not None:
         raise ShowNotFoundException(f"{show_name} show not found")
    return [ShowsOut.entity_to_model(q) for q in result]


@router.post("/")
async def upsert_shows(session: Annotated[AsyncSession, Depends(get_session)], show: ShowsIn) -> ShowsOut:
    show_entity = Shows(show_name=show.show_name, genre=show.genre)
    show_entity.characters.extend(
        [Characters(ch_name=ch.ch_name, role=ch.role, show_id=show_entity.show_id, shows=show_entity) for ch in
         show.characters])
    session.add(show_entity)
    await session.commit()
    await session.refresh(show_entity)
    return ShowsOut.entity_to_model(show_entity)

path = os.path.expanduser('~/PycharmProjects/PythonProject/resources')
# path = Path(__file__).resolve().parent.parent.parent.__str__() + '/resources' #routers -> RestAPI -> PythonProject
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
templates = Jinja2Templates(directory=path)


@router.get("/{show_name}", response_class=HTMLResponse)
async def read_show(session: Annotated[AsyncSession, Depends(get_session)], request: Request, show_name: str):
    subquery = select(Shows).where(Shows.show_name == show_name).subquery()
    stmt = select(Characters).join(subquery)
    result = await session.execute(stmt)
    characters = CharactersOut.entities_to_models(result.scalars().all())
    return templates.TemplateResponse(
        "show.html",
        {
            "request": request,
            "show_name": show_name,
            "characters": characters
        }
    )
