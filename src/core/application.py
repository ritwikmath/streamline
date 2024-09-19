from core.dataTypes import Dictionary
from core.protocols import LoggerProtocol, CacheProtocol
from http_router import Router


class Application:
    instance = None
    __config = Dictionary()

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, kwargs: dict):
        for item in kwargs.items():
            key, value = item[0], item[1]
            self.__config[key] = value
    
    @property
    def cache(self) -> CacheProtocol:
        return self.__cache

    @cache.setter
    def cache(self, driver, /):
        self.__cache = driver
    
    @property
    def logger(self) -> LoggerProtocol:
        return self.__logger

    @logger.setter
    def logger(self, driver, /):
        self.__logger = driver
    
    @property
    def router(self) -> Router:
        return self.__router

    @router.setter
    def router(self, driver, /):
        self.__router = driver


app = Application()
