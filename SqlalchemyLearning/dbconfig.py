from sqlalchemy import create_engine
from EnvironmentConfig import get_db_url

_engine = None

def get_engine():
    global _engine
    if _engine is None:
        db_url = get_db_url()
        if db_url is None:
            raise ValueError("DB_URL not found in environment variables")
        _engine = create_engine(db_url, echo=True)
    return _engine