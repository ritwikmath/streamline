import os
from config.interface import ConfigInterface


class AuthConfig(ConfigInterface):
    def get_configurations(self) -> object:
        return {
            "AUTH_TYPE": os.getenv("AUTH_TYPE", "Bearer"),
            "PASSWORD_TIMEOUT": os.getenv("PASSWORD_TIMEOUT", None)
        }
