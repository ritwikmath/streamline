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
        cache_driver = importlib.import_module("core.cacheDriver")
        app.cache = getattr(cache_driver, f"{cache_driver_name.capitalize()}Cache")
    except KeyError:
        app.logger.warn("Cache support is not available for this application")

def load_logger():
    app.logger = Logger().logger

def load_router():
    app.router = Router()

def load_db(config):
    try:
        db_driver_name = config["default"]["database"]
        db_driver = importlib.import_module("core.dbDriver")
        app.db = getattr(db_driver, f"{db_driver_name.capitalize()}Client")
    except KeyError:
        app.logger.warn("Database support is not available for this application")

class Bootstrap:
    def __init__(self):
        Config()
        config = configparser.ConfigParser()
        config.read(os.path.join(app.config.APP_ROOT, "config.ini"))
        load_logger()
        load_config(config)
        load_router()
        load_db(config)
        importlib.import_module("controllers")
