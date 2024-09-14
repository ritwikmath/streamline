from abc import ABC, abstractmethod


class Config(ABC):
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