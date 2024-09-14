import os
from config.interface import ConfigInterface


class CacheConfig(ConfigInterface):
    def get_configurations(self) -> dict:
        return {
            "STORES": {
                "local": {

                },
                "file": {
                    "path": os.getenv("CACHE_FILE_LOCATION", "resources/cache"),
                    "name": os.getenv("CACHE_FILE_NAME", "cache.json")
                },
                "database": {
                    "table": os.getenv("CACHE_TABLE", "cache")
                },
                "redis": {
                    "host":  os.getenv("REDIS_HOST", "localhost"),
                    "port": os.getenv("REDIS_PORT", 6379)
                }
            }
        }
