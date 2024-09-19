from core.application import app
from core.configs import Config
from core.logDriver import Logger
import configparser
import os
import importlib
from http_router import Router


def load_config(config):
    try:
        cache_driver_name = config["default"]["cache"]
    except:
        cache_driver_name = "local"
    cache_driver = importlib.import_module("core.cacheDriver")
    app.cache = getattr(cache_driver, f"{cache_driver_name.capitalize()}Cache")

def load_logger():
    app.logger = Logger().logger

def load_router():
    app.router = Router()

class Bootstrap:
    def __init__(self):
        Config()
        config = configparser.ConfigParser()
        config.read(os.path.join(app.config.APP_ROOT, "config.ini"))
        load_logger()
        load_config(config)
        load_router()
