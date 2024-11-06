from typing import Protocol
from sqlalchemy.orm import Session

class LoggerProtocol(Protocol):
    def info(self, message: str) -> str:
        ...
    
    def warn(self, message: str) -> str:
        ...
    
    def debug(self, message: str) -> str:
        ...

    def error(self, message: str) -> str:
        ...

class CacheProtocol(Protocol):
    def store_value(self, key: str, value: any) -> None:
        ...
    
    def get_value(self, key: str) -> any:
        ...

class DBProtocol(Protocol):
    def client(self) -> Session:
        ...