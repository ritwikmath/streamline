from core.application import Application
from bootstrap.bootstrap import Bootstrap


app = Application()
Bootstrap()


if __name__ == "__main__":
    app.cache.store_value("surname", "math")
    app.logger.debug(app.cache.get_value("surname"))
    @app.router.route('/simple/{var}')
    def simple(params):
        app.logger.info(params)
        return 'result from the fn' 
    match = app.router('/simple/12', method='GET')
    app.logger.debug(match.target(match.params))
