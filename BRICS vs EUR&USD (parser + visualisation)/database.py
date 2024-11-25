from config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncAttrs
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, String, create_engine


sync_engine = create_engine(
    url=settings.get_sync_db_url,
    echo=True
)

async_engine = create_async_engine(
    url=settings.get_async_db_url,
    echo=True,
)

sync_session_factory = sessionmaker(sync_engine)

async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):

    __abstarct__ = True

    repr_cols_num = 3
    repr_cols = tuple()
    
    def __repr__(self):
        """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"


