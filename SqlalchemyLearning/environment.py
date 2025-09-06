print("Inside environment.py")
import sys
import os
from dotenv import load_dotenv

_instance = None

class EnvConfig:
    def __init__(self):
        self.db_url = None
        self.db_schema = None

    def schema_args(self):
        if self.db_url.startswith("postgresql"):
            return {"schema": self.db_schema}
        return {}


def get_env_config():
    global _instance
    if _instance is None:
        print("Creating EnvironmentConfig Singleton")
        env = os.getenv("APP_ENV", "dev")
        dotenv_path = f"../resources/.env.{env}"
        load_dotenv(os.path.expanduser(dotenv_path))
        _instance = EnvConfig()
        _instance.db_url = os.getenv("DB_URL")
        _instance.db_schema = os.getenv("DB_SCHEMA", "")
        if _instance.db_url is None:
            raise ValueError("DB_URL not found")
        print("Created EnvironmentConfig Singleton")
    return _instance

env_config = get_env_config()
print("Modules loaded by now: ", sys.modules.get("SqlalchemyLearning"))
