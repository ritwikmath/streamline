import os
import importlib
from core.application import app

for file in os.listdir(os.path.join(app.config.APP_ROOT, "controllers")):
    if ".py" not in file or file == "__init__.py":
        continue
    module = file[:-3]
    importlib.import_module(f"controllers.{module}")
