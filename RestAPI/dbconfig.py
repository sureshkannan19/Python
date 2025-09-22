import logging
from typing import  AsyncIterator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from RestAPI.entities import Base
from RestAPI.environment import env_config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class DatabaseConfig:
    _instance = None
    _engine = None
    _async_session_factory = None

    def __new__(cls):
        if cls._instance is None:
            logging.info("Creating Database singleton..")
            cls._instance = super(DatabaseConfig, cls).__new__(cls)
            logging.info("Database creation completed")
        return cls._instance

    async def initialize_engine(self):
        if self._engine is None:
            logging.info("Initializing DB engine")
            self._engine = create_async_engine(env_config.db_url, echo=True)
            async with self._engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            logging.info("DB engine created")
            self._async_session_factory = async_sessionmaker(
                bind=self._engine, class_=AsyncSession, expire_on_commit=False
            )
        return self._engine

    async def get_engine(self):
        await self.initialize_engine()
        return self._engine

    @property
    def async_session_factory(self):
        return self._async_session_factory


async def get_session() -> AsyncIterator[AsyncSession]:
    db_config = DatabaseConfig()
    await db_config.initialize_engine()
    async with db_config.async_session_factory() as session:
        logging.info("Async Session Created")
        yield session
        logging.info("Async Session Closed")