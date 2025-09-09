from fastapi import FastAPI

import uvicorn
from routers.showsapi import show_router
from routers.quotesapi import quote_router
from routers.basicapi import router

app = FastAPI(title="API Learning")
app.include_router(router)
app.include_router(quote_router)
app.include_router(show_router)

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)