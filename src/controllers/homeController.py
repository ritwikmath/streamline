from core.application import app

@app.router.get('/simple/{var}')
def simple(var):
    app.cache.store_value("surname", "math")
    app.logger.info(app.cache.get_value("surname"))
    app.logger.info(var)
    return 'result from the fn'