from core.application import app
from core.configs import Config
import configparser
import os
import importlib


def load_config():
    config = configparser.ConfigParser()
    config.read(os.path.join(app.config.app["ROOT"], "config.ini"))
    cache_driver_name = config["default"]["cache"]
    cache_driver = importlib.import_module("core.cacheDriver")
    app.cache = getattr(cache_driver, f"{cache_driver_name.capitalize()}Cache")


class Bootstrap:
    def __init__(self):
        Config()
        load_config()
