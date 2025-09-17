from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Annotated

from starlette import status

from RestAPI.dbconfig import get_session
from RestAPI.entities import Users
from RestAPI.schemas import UserOut, UserIn


URL_PREFIX = "/users"
router = APIRouter(prefix=URL_PREFIX)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@router.get("/me")
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],
          session: Annotated[Session, Depends(get_session)]):
    query = select(Users).where(Users.user_name == token)
    user: Users = session.execute(query).scalar_one_or_none()
    if user:
        return UserOut.entity_to_model(user)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")
@router.post("/")
def root(session: Annotated[Session, Depends(get_session)],
         user_input : UserIn) -> UserOut:
    user = UserIn.model_to_entity(user_input)
    session.add(user)
    session.commit()
    session.refresh(user)
    return UserOut.entity_to_model(user)