from core.application import app
from core.cacheDriver import FileCache
from core.configs import Config


def load_config():
    app.cache = FileCache


class Bootstrap:
    def __init__(self):
        Config()
        load_config()
