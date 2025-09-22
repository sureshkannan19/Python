from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from RestAPI.dbconfig import get_session
from RestAPI.entities import Users

router = APIRouter(prefix="/token")


@router.post("/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
          session: Annotated[AsyncSession, Depends(get_session)]):
    query = select(Users).where(Users.user_name == form_data.username)
    result = await session.execute(query)
    user: Users = result.scalar_one_or_none()
    if user and user.verify_password(form_data.password):
        return {"access_token": user.user_name, "token_type": 'bearer'}
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
