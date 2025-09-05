from sqlalchemy import select
from dbconfig import get_engine
from SqlalchemyLearning.entities import Quotes

print("Inside SqlAlchemyLearning")
with get_engine().connect() as conn:
    result = conn.execute(select(Quotes))
    print(result.fetchone())