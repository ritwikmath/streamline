import json
import os
from .application import app
from .interfaces import Config


class LocalCache(Config):
    store = {}

    @classmethod
    def store_value(cls, **kwargs):
        for key, value in kwargs.items():
            cls.store[key] = value

    @classmethod
    def get_value(cls, key: str) -> any:
        return cls.store[key]


class FileCache(Config):
    @classmethod
    def get_file_path(cls):
        path, file_name = app.config.cache["file"].values()
        file_path = os.path.join(app.config.app["ROOT"], path, file_name)
        return file_path

    @classmethod
    def store_value(cls, key, value, /):
        file_path = cls.get_file_path()
        with open(file_path, "r") as file:
            data = json.load(file)

        data[key] = value

        with open(file_path, "w") as file:
            json.dump(data, file, indent=2)
            file.truncate()

    @classmethod
    def get_value(cls, key: str) -> any:
        file_path = cls.get_file_path()
        with open(file_path, "r") as file:
            data = json.load(file)
            value = data.get(key)
        return value
