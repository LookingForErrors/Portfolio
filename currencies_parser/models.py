import datetime
from typing import Annotated
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, text, CheckConstraint, Index, Float, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base



intpk = Annotated[int, mapped_column(primary_key=True)]



class CurrenciesOrm(Base):
    __tablename__ = "currency_table"

    id: Mapped[intpk]
    currency_from: Mapped[str] 
    currency_to: Mapped[str] 
    value: Mapped[float]
    date: Mapped[datetime.datetime] 


metadata_obj = MetaData()

currency_table = Table(
    "currency_table",
    metadata_obj,
    Column("currency_from", String),
    Column("currency_to", String),
    Column("value", Float),
    Column("date",Date),
)

