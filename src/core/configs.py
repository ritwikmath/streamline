from config.cache import CacheConfig
from config.app import AppConfig
from core.application import app


class Config:
    def __init__(self) -> None:
        self.__load_configurations()

    @staticmethod
    def __load_configurations() -> None:
        app.config.cache = CacheConfig().get_configurations()["STORES"]
        app.config.app = AppConfig().get_configurations()

