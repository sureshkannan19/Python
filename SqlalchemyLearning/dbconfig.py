from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

env = os.getenv("APP_ENV", "prod")
dotenv_path = f"../resources/.env.{env}"
load_dotenv(os.path.expanduser(dotenv_path))
DB_URL = os.getenv("DB_URL")
DB_SCHEMA = os.getenv("DB_SCHEMA", "")

engine = create_engine(DB_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

def schema_args():
    if DB_URL.startswith("postgresql"):
        return {"schema": DB_SCHEMA}
    return {}
