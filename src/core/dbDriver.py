from core.interfaces import DatabaseInterface
from core.application import app

if app.config.database_driver:
    from sqlalchemy import create_engine
    from contextlib import contextmanager
    from sqlalchemy.orm import Session


class PostgresClient(DatabaseInterface):
    __engine = None
    
    @classmethod
    def connect(cls):
        if cls.__engine is None:
            db_config = app.config.db["postgres"]
            cls.__engine = create_engine(f"postgresql+psycopg://{db_config['user']}:{db_config['pwd']}@{db_config['host']}:{db_config['port']}/{db_config['db']}")
    
    @classmethod
    def client(cls) -> Session:
        cls.connect()
        session = Session(bind=cls.__engine)
        return session


class DynamoClient(DatabaseInterface):

    @classmethod
    def client(cls):
        ...
