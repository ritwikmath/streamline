from abc import ABC, abstractmethod


class CacheInterface(ABC):
    @classmethod
    @abstractmethod
    def store_value(cls, **kwargs) -> None:
        ...

    @classmethod
    @abstractmethod
    def get_value(cls, **kwargs) -> None:
        ...


class ConfigInterface(ABC):
    @abstractmethod
    def get_configurations(self) -> object:
        ...


class DatabaseInterface(ABC):
    @classmethod
    @abstractmethod
    def connect(cls):
        ...
    
    @classmethod
    @abstractmethod
    def client(cls) -> any:
        ...
