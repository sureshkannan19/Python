import os
from pathlib import Path

from dotenv import load_dotenv

_instance = None

class EnvConfig:
    def __init__(self, db_url: str, db_schema: str, env: str, dotenv_path: Path):
        self.db_url = db_url
        self.db_schema = db_schema
        self.env = env
        self.dotenv_path = dotenv_path

    def schema_args(self):
        if self.db_url.startswith("postgresql"):
            return {"schema": self.db_schema}
        return {}


def get_env_config():
    global _instance
    if _instance is None:
        print("Creating EnvironmentConfig Singleton")
        env = os.getenv("APP_ENV", "prod")
        base_dir = Path(__file__).resolve().parent.parent
        dotenv_path = base_dir / "resources" / f".env.{env}"
        load_dotenv(os.path.expanduser(dotenv_path))
        _instance = EnvConfig(os.getenv("DB_URL"), os.getenv("DB_SCHEMA", ""), env, dotenv_path)
        if _instance.db_url is None:
            raise ValueError("DB_URL not found")
        print("Created EnvironmentConfig Singleton with DB_SCHEMA=", _instance.db_schema)
    return _instance

env_config = get_env_config()
