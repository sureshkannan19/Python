from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from SqlalchemyLearning.EnvironmentConfig import schema_args


class Base(DeclarativeBase):
    pass

class Quotes(Base):
    __tablename__ = 'quotes'
    __table_args__ = schema_args()

    id: Mapped[int] = mapped_column(primary_key=True)
    quote: Mapped[str] = mapped_column(String)
    source: Mapped[str] = mapped_column(String)