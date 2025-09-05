import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root() -> dict[str, str]:
    return {'message': "Welcome SK!"}


@app.get("/identify")
def welcome(name: str | None = None,
            age: int | None = None) -> dict[str, str]:
    return {'message': f"I'm {name}, and {age} years old"}


@app.get("/welcome/{name}")
def welcome(name: str | None = None) -> dict[str, str]:
    if name == 'Hope':
        raise HTTPException(status_code=404, detail=f"{name}, you are not welcomed.")
    return {'message': f"Welcome {name}"}


if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)