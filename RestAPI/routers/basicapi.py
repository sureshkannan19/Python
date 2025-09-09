from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
def root() -> dict[str, str]:
    return {'message': "Welcome SK!"}


@router.get("/identify")
def welcome(name: str | None = None,
            age: int | None = None) -> dict[str, str]:
    return {'message': f"I'm {name}, and {age} years old"}


@router.get("/welcome/{name}")
def welcome(name: str | None = None) -> dict[str, str]:
    if name == 'Hope':
        raise HTTPException(status_code=404, detail=f"{name}, you are not welcomed.")
    return {'message': f"Welcome {name}"}
