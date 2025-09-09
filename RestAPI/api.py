from fastapi import FastAPI

import uvicorn
from routers import showsapi, quotesapi, basicapi
app = FastAPI(title="API Learning")
app.include_router(basicapi.router)
app.include_router(quotesapi.router)
app.include_router(showsapi.router)

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)