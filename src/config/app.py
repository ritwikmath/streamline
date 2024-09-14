import os
import sys
from config.interface import ConfigInterface


class AppConfig(ConfigInterface):
    def get_configurations(self) -> object:
        return {
            "APP_NAME": os.getenv("APP_NAME", "API_FIRST"),
            "ENV": os.getenv("ENV", "staging"),
            "DEBUG": os.getenv("DEBUG", False),
            "CIPHER": os.getenv("CIPHER", "Base64"),
            "ROOT": os.path.abspath(sys.modules["__main__"].__file__.rstrip("main.py"))
        }
