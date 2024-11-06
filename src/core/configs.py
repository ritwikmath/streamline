from config import *
from core.application import app
from core.dataTypes import Dictionary


class Config:
    def __init__(self) -> None:
        self.__load_configurations()

    @staticmethod
    def __load_configurations() -> None:
        app.config = Dictionary({
            "cache": CacheConfig().get_configurations()["STORES"],
            "logging": LogConfig().get_configurations(),
            "db": DBConfig().get_configurations()["DRIVERS"],
        })
        app.config = Dictionary(AppConfig().get_configurations())

