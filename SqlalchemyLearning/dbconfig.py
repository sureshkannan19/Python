print("Inside dbconfig.py")

from sqlalchemy import create_engine
from SqlalchemyLearning.entities import Base
from SqlalchemyLearning.environment import env_config


class DatabaseConfig:

    _instance = None
    _engine = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConfig, cls).__new__(cls)
        return cls._instance

    def initialize_engine(self):
        if self._engine is None:
            print("Initializing DB engine")
            self._engine = create_engine(env_config.db_url, echo=True)
            Base.metadata.create_all(bind=self._engine)
            print("DB engine created")
        return self._engine

    def get_engine(self):
        return self.initialize_engine()