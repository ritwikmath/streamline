from core.application import app


@app.router.get('/simple/{var}')
def simple(var):
    return {"param": var}, 200


@app.router.post('/simple')
def simple_store():
    payload = app.request.json
    app.cache.store_value("surname", "math")
    app.logger.info(app.cache.get_value("surname"))
    return {"message": payload, "surname": app.cache.get_value("surname")}, 200
