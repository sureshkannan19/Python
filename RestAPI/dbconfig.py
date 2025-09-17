import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from RestAPI.entities import Base
from RestAPI.environment import env_config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def get_session():
    with Session(DatabaseConfig().get_engine()) as session:
        logging.info("Session Created")
        yield session
        logging.info("Session Closed")

class DatabaseConfig:

    _instance = None
    _engine = None

    def __new__(cls):
        if cls._instance is None:
            logging.info("Creating Database singleton..")
            cls._instance = super(DatabaseConfig, cls).__new__(cls)
            logging.info("Database creation completed")
        return cls._instance

    def initialize_engine(self):
        if self._engine is None:
            logging.info("Initializing DB engine")
            self._engine = create_engine(env_config.db_url, echo=True)
            Base.metadata.create_all(bind=self._engine)
            logging.info("DB engine created")
        return self._engine

    def get_engine(self):
        return self.initialize_engine()