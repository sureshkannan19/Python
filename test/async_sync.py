import uvicorn
from fastapi import FastAPI
from async_sync_router import async_sync_router

app = FastAPI(title="async test")
app.include_router(async_sync_router)


if __name__ == "__main__":
    uvicorn.run("async_sync:app", host="127.0.0.1", port=9090)
