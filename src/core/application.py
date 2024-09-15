from core.dataTypes import Dictionary


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
    def cache(self):
        return self.__cache

    @cache.setter
    def cache(self, driver, /):
        self.__cache = driver

    def serve(self, *args, **kwargs):
        ...


app = Application()
