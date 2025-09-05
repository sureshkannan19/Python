from sqlalchemy import select
from SqlalchemyLearning.entities import Quotes, Base
from dbconfig import engine

Base.metadata.create_all(bind=engine)

with engine.connect() as conn:
    result = conn.execute(select(Quotes))
    print(result.fetchone())
