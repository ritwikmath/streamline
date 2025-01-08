import configparser
import os
import importlib
import json

import boto3.session
from core.application import app
from core.configs import Config
from core.logDriver import Logger
from http_router import Router
import boto3
from botocore.exceptions import ClientError


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


def load_secrets():
    secret_name = "CONFIG"
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name="ap-south-1"
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )

    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
        elif e.response['Error']['Code'] == 'DecryptionFailure':
            print("The requested secret can't be decrypted using the provided KMS key:", e)
        elif e.response['Error']['Code'] == 'InternalServiceError':
            print("An error occurred on service side:", e)
    else:
        secret_dict = json.loads(get_secret_value_response["SecretString"])
        for key, val in secret_dict.items():
            os.environ[key] = val


class Bootstrap:
    def __init__(self):
        load_secrets()
        Config()
        config = configparser.ConfigParser()
        config.read(os.path.join(app.config.APP_ROOT, "config.ini"))
        load_logger()
        load_config(config)
        load_router()
        load_db(config)
        importlib.import_module("controllers")
