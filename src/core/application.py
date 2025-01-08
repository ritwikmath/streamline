import json
from .dataTypes import Dictionary
from .protocols import LoggerProtocol, CacheProtocol, DBProtocol, RequestProtocol
from http_router import Router
from pydantic import ValidationError
from .wrappers import parse_event


class Application:
    instance = None
    __config = Dictionary()
    __cache = None
    __before_request = []
    __db = None
    __router = None
    __logger = None
    __request = None

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
        if not self.__cache:
            raise AttributeError("Cache is not instantiated for this application")
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
    
    @property
    def db(self) -> DBProtocol:
        return self.__db

    @db.setter
    def db(self, driver, /):
        self.__db = driver

    @property
    def request(self) -> RequestProtocol:
        return self.__request

    @request.setter
    def request(self, data, /):
        self.__request = data
    

    @parse_event
    def handle(self, path, method, payload, /):
        match = self.router(path, method)
        app.request = Dictionary({
            "json": payload,
            "url": path
        })
        params = match.params or {}
        response = None
        try:
            response = match.target(**params)
            self.logger.info(f"Data: {response[0]}, status: {response[1]}")
            return {
                "body": json.dumps(  # Body
                    response[0]
                ),
                "statusCode": int(response[1])  # Status code
            }
        except ValidationError as ex:
            self.logger.error(ex)
        except KeyError as key_ex:
            self.logger.error(str(key_ex))
            self.logger.error(f"""Response type is not valid. Controller {match.target.__name__} returned \
{type(response).__name__} instead of a tuple""")
            raise Exception("Response type is not valid")
        except ValueError as value_ex:
            self.logger.error(f"""Response status is not valid. Controller {match.target.__name__} \
returned {response[1]} instead of a int""")
            raise Exception("Response type is not valid")


app = Application()
