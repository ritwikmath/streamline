from core.interfaces import DatabaseInterface
from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import Session
from core.application import app

class PostgresClient(DatabaseInterface):
    __engine = None
    
    @classmethod
    def connect(cls):
        if cls.__engine == None:
            db_config = app.config.db["postgres"]
            cls.__engine = create_engine(f"postgresql+psycopg://{db_config["user"]}:{db_config["pwd"]}@{db_config["host"]}:{db_config["port"]}/{db_config["db"]}")
    
    @classmethod
    def client(cls) -> Session:
        cls.connect()
        session = Session(bind=cls.__engine)
        return session


class DynamoClient(DatabaseInterface):
    def connect(cls):
        if cls.__engine == None:
            cls.__engine = create_engine("postgresql+psycopg://scott:tiger@localhost/test")

    def client(cls):
        cls.connect()
        session = Session(bind=cls.__engine)
        yield session
        session.commit()
        session.close()