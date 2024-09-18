import os
from core.interfaces import ConfigInterface
import logging


class LogConfig(ConfigInterface):
    def get_configurations(self) -> dict:
        level = {
            "DEBUG": logging.DEBUG
        }
        
        return {
            "level": level.get(os.getenv("LOG_LEVEL", "debug").upper()),
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s"
        }
