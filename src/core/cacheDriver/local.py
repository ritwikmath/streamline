from core.interfaces import CacheInterface

class LocalCache(CacheInterface):
    store = {}

    @classmethod
    def store_value(cls, key, value, /):
        cls.store[key] = value

    @classmethod
    def get_value(cls, key: str) -> any:
        return cls.store[key]
