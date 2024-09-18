from core.application import Application
from bootstrap.bootstrap import Bootstrap


app = Application()
Bootstrap()


if __name__ == "__main__":
    app.cache.store_value("surname", "math")
    app.logger.debug(app.cache.get_value("surname"))
    
