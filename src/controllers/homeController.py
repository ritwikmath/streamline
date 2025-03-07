from core.application import app
from database.models.userAccount import User
from validators.UserValidator import UserValidator


@app.router.get('/simple/{var}')
def simple(var):
    return {"param": var}, 200


@app.router.post('/simple')
def simple_store():
    app.logger.info(f"Started processing request_id: {app.request.request_id}")
    payload = app.request.json
    result = None
    with app.db.client() as db_session:
        result = db_session.query(User).all()
        response = [UserValidator.model_validate(user).model_dump_json() for user in result]
        return {"message": payload, "data": response}, 200
