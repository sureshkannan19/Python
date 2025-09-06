from sqlalchemy import select
from sqlalchemy.orm import Session

from dbconfig import DatabaseConfig
from SqlalchemyLearning.entities import Quotes

engine = DatabaseConfig().get_engine()
print("Inside SqlAlchemyLearning")
with engine.connect() as conn:
    result = conn.execute(select(Quotes))
    print(result.fetchone())

quotes = Quotes(quote="What do you really desire?", source="Lucifer")
with Session(engine) as session:
    # session.add(quotes)
    # session.commit()

    stmt = select(Quotes).where(Quotes.source == "Lucifer")
    print(session.execute(stmt).scalars().all())