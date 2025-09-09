from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from RestAPI.environment import env_config


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

class Shows(Base):
    __tablename__ = 'shows'
    __table_args__ = env_config.schema_args()

    show_id: Mapped[int] = mapped_column(primary_key=True)
    show_name: Mapped[str] = mapped_column(String)
    genre: Mapped[str] = mapped_column(String)
    characters: Mapped[List["Characters"]] = relationship(back_populates="shows")

    def __repr__(self):
        return f"<Shows(show_id={self.show_id}, show_name={self.show_name}, genre={self.genre})>"


class Characters(Base):
    __tablename__ = 'characters'
    __table_args__ = env_config.schema_args()
    schema_name = env_config.schema_args().get("schema")

    ch_id: Mapped[int] = mapped_column(primary_key=True)
    ch_name: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)
    show_id: Mapped[int] = mapped_column(ForeignKey(f'{schema_name}.shows.show_id'))
    shows : Mapped["Shows"] = relationship(back_populates="characters")

    def __repr__(self):
        return f"<Characters(ch_id={self.ch_id}, ch_name={self.ch_name}, role={self.role}, show_id={self.show_id})>"