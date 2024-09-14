from abc import ABC, abstractmethod


class ConfigInterface(ABC):
    @abstractmethod
    def get_configurations(self) -> object:
        ...