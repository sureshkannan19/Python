from RestAPI.routers.authapi import router as auth_router
from RestAPI.routers.basicapi import router as basic_router
from RestAPI.routers.quotesapi import router as quotes_router
from RestAPI.routers.showsapi import router as shows_router
from RestAPI.routers.usersapi import router as users_router

__all__ = ["users_router", "shows_router", "quotes_router", "auth_router", "basic_router"]
