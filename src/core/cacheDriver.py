import os
import pickle
import redis
from redis.cluster import RedisCluster
from core.application import app
from core.interfaces import CacheInterface


class LocalCache(CacheInterface):
    store = {}

    @classmethod
    def store_value(cls, key, value, /):
        cls.store[key] = value

    @classmethod
    def get_value(cls, key: str) -> any:
        return cls.store[key]


class FileCache(CacheInterface):
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
    def get_value(cls, key: str, /) -> any:
        file_path = cls.__get_file_path()
        try:
            with open(file_path, "rb") as file:
                data = pickle.load(file)
                value = data.get(key)
            return value
        except EOFError:
            return None


class RedisCache(CacheInterface):
    __redis = None
    
    @classmethod
    def __get_connection(cls):
        if not cls.__redis:
            host=app.config.cache["redis"]["host"]
            port=app.config.cache["redis"]["port"]
            # Attempt to connect to the Redis server
            # cls.__redis = redis.Redis(
            #     host=host,
            #     port=port,
            #     decode_responses=True,
            #     socket_connect_timeout=1,
            #     socket_timeout=1
            # )

            # Attempt to connect to the Redis cluster
            cls.__redis = RedisCluster(
                host=host,
                port=port,
                decode_responses=True,
                ssl=True,
                ssl_cert_reqs="none",
                socket_connect_timeout=1,
                socket_timeout=1
            )
        return cls.__redis

    @classmethod
    def store_value(cls, key, value, /):
        key_structure = key.split(":")
        if len(key_structure) == 1:
            key_name, expire, exp_time = key_structure[0], None, None
        elif len(key_structure) == 3:
            key_name, expire, exp_time = key.split(":") 
        else:
            raise ValueError("Wrong structure. Sample: key_name:ex:10")
        redis_conn = cls.__get_connection()
        if expire:
            if expire == "ex":
                redis_conn.setex(key_name, exp_time, value)
            elif expire == "px":
                redis_conn.psetex(key_name, exp_time, value)
            else:
                raise ValueError("Redis expiration supports ex & px. Sample: key_name:ex:10")
        else:
            redis_conn.set(key_name, value)

    @classmethod
    def get_value(cls, key: str, /) -> any:
        redis_conn = cls.__get_connection()
        return redis_conn.get(key)
