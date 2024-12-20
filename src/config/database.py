import os
from core.interfaces import ConfigInterface


class DBConfig(ConfigInterface):
    def get_configurations(self) -> dict:
        return {
            "DRIVERS": {
                "postgres": {
                    "host": os.getenv("DB_HOST", "localhos"),
                    "port": os.getenv("DB_PORT", "5432"),
                    "user": os.getenv("DB_USER", "postgres"),
                    "pwd": os.getenv("DB_PASSWORD", "secret"),
                    "db": os.getenv("DB_NAME", "postgres")
                },
                "dynamo": {
                    
                },
                "mongo": {
                    "host": os.getenv("DB_HOST", "localhost"),
                    "port": os.getenv("DB_PORT", "5432"),
                    "user": os.getenv("DB_USER", "lambda_user"),
                    "pwd": os.getenv("DB_PASSWORD", "secret"),
                    "db": os.getenv("DB_NAME", "lambda")
                },
                "mysql": {
                    "host": os.getenv("DB_HOST", "localhost"),
                    "port": os.getenv("DB_PORT", "27017"),
                    "user": os.getenv("DB_USER", "lambda_user"),
                    "pwd": os.getenv("DB_PASSWORD", "secret"),
                    "tls": os.getenv("DB_TLS", False)
                }
            }
        }
