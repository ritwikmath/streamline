from core.interfaces import DatabaseInterface
from core.application import app
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from collections.abc import Iterator
from contextlib import contextmanager

class PostgresClient(DatabaseInterface):
    __engine = None
    
    @classmethod
    def connect(cls):
        if cls.__engine is None:
            db_config = app.config.db["postgres"]
            cls.__engine = create_engine(f"postgresql+psycopg://{db_config['user']}:{db_config['pwd']}@{db_config['host']}:{db_config['port']}/{db_config['db']}")
    
    @classmethod
    @contextmanager
    def client(cls) -> Iterator[Session]:
        cls.connect()
        session = Session(bind=cls.__engine)
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()