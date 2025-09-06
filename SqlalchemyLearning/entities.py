print("Inside entities.py")

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from environment import env_config


class Base(DeclarativeBase):
    pass

class Quotes(Base):
    __tablename__ = 'quotes'
    __table_args__ = env_config.schema_args()

    id: Mapped[int] = mapped_column(primary_key=True)
    quote: Mapped[str] = mapped_column(String)
    source: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"<Quote(id={self.id}, quote={self.quote}, source={self.source})>"