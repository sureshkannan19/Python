import logging
import time

from fastapi import FastAPI

import uvicorn
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware

from RestAPI.exceptions.exceptions import ShowNotFoundException
from RestAPI.routers import shows_router, auth_router, quotes_router, users_router, basic_router

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
app = FastAPI()
app = FastAPI(title="API Learning")
app.include_router(shows_router)
app.include_router(auth_router)
app.include_router(quotes_router)
app.include_router(users_router)
app.include_router(basic_router)

# Global Exception handler
@app.exception_handler(ShowNotFoundException)
async def exception_handler(request: Request, exception: ShowNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": str(exception)}
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_cookies(request: Request, call_next):
    logging.info(f"Request headers {request.headers}")
    before = time.perf_counter()
    response = await call_next(request)
    after = time.perf_counter()
    logging.info(f"Request took {after - before} seconds")
    response.set_cookie(key="shows_cookie", value="show_details")
    # response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)
