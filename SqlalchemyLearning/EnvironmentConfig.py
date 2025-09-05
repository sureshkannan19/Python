import os
from dotenv import load_dotenv

_db_url = None
_db_schema = None

def _load_config():
    global _db_url, _db_schema
    if _db_url is None and _db_schema is None:
        print("Populating environment variables...")
        _db_url = os.environ.get("DB_URL")
        env = os.getenv("APP_ENV", "prod")
        dotenv_path = f"../resources/.env.{env}"
        load_dotenv(os.path.expanduser(dotenv_path))
        _db_url = os.getenv("DB_URL")
        _db_schema = os.getenv("DB_SCHEMA", "")
        print("Done")
    return _db_url, _db_schema


def get_db_url():
    db_url, _ = _load_config()
    return db_url


def get_db_schema():
    _, db_schema = _load_config()
    return db_schema


def schema_args():
    db_url, db_schema = _load_config()
    if db_url.startswith("postgresql"):
        return {"schema": db_schema}
    return {}
