import json
import os
from core.application import app
from core.interfaces import Config
import pickle


class LocalCache(Config):
    store = {}

    @classmethod
    def store_value(cls, key, value, /):
        cls.store[key] = value

    @classmethod
    def get_value(cls, key: str) -> any:
        return cls.store[key]


class FileCache(Config):
    @classmethod
    def __get_file_path(cls):
        path, file_name = app.config.cache["file"].values()
        file_path = os.path.join(app.config.APP_ROOT, path, file_name)
        return file_path

    @classmethod
    def store_value(cls, key, value, /):
        file_path = cls.__get_file_path()
        try:
            with open(file_path, "rb") as file:
                data = pickle.load(file)
        except EOFError:
            data = {}

        data[key] = value

        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            file.truncate()

    @classmethod
    def get_value(cls, key: str) -> any:
        file_path = cls.__get_file_path()
        try:
            with open(file_path, "rb") as file:
                data = pickle.load(file)
                value = data.get(key)
            return value
        except EOFError:
            return None


class RedisCache(Config):
    @classmethod
    def __get_file_path(cls):
        path, file_name = app.config.cache["file"].values()
        file_path = os.path.join(app.config.APP_ROOT, path, file_name)
        return file_path

    @classmethod
    def store_value(cls, key, value, /):
        file_path = cls.__get_file_path()
        try:
            with open(file_path, "rb") as file:
                data = pickle.load(file)
        except EOFError:
            data = {}

        data[key] = value

        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            file.truncate()

    @classmethod
    def get_value(cls, key: str) -> any:
        file_path = cls.__get_file_path()
        try:
            with open(file_path, "rb") as file:
                data = pickle.load(file)
                value = data.get(key)
            return value
        except EOFError:
            return None