import logging
from core.application import app

class Logger:
    __logger = None

    def __init__(self) -> None:
        logging.basicConfig(format=app.config.logging["format"], level=app.config.logging["level"])
        self.__logger = logging.getLogger("streamline_logger")
        
    @property
    def logger(self):
        return self.__logger
