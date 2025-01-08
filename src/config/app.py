import os
import sys
from core.interfaces import ConfigInterface
from pathlib import Path


class AppConfig(ConfigInterface):
    def __init__(self):
        self.file_path = Path(__file__).resolve()

    def get_configurations(self) -> object:
        file_path = Path(__file__).resolve()

        return {
            "APP_NAME": os.getenv("APP_NAME", "API_FIRST"),
            "ENV": os.getenv("ENV", "staging"),
            "DEBUG": os.getenv("DEBUG", False),
            "CIPHER": os.getenv("CIPHER", "Base64"),
            "APP_ROOT": self.file_path.parent.parent
        }
