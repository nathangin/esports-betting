from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from loguru import logger

from config import DATABASE_URL
from db.models import Base


_engine = None
_SessionLocal = None


def get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(
            DATABASE_URL,
            echo=False,
            connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
        )
    return _engine


def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)
    logger.info(f"Database initialized at {DATABASE_URL}")
    return engine


def get_session_factory():
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(bind=get_engine(), expire_on_commit=False)
    return _SessionLocal


@contextmanager
def get_session() -> Session:
    factory = get_session_factory()
    session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
