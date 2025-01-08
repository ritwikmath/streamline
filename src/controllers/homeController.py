from core.application import app
from sqlalchemy import select
from database.models.userAccount import User
from sqlalchemy import update
from validators.UserValidator import UserValidator


@app.router.get('/simple/{var}')
def simple(var):
    with app.db.client() as session:
        stmt = select(User)
        response = session.scalars(stmt)
        session.close()
    # app.cache.store_value("surname", "math")
    # app.logger.info(app.cache.get_value("surname"))
    app.logger.info(response)
    return 'result from the fn'


@app.router.post('/simple')
def simple_store():
    payload = app.request.json
    app.cache.store_value("surname", "math")
    app.logger.info(app.cache.get_value("surname"))
    # with app.db.client() as session:
    #     validated_user = UserValidator(**payload)
    #     spongebob = User(**validated_user.model_dump())
    #     session.add(spongebob)
    #     query = select(User)
    #     for user in session.scalars(query):
    #         app.logger.info(user)
    #     response = f"{spongebob}"
    #     print(response)
    #     session.commit()
    #     session.close()
    return {"message": "Hello"}, 200


@app.router.patch('/simple/{var}')
def simple_update(var):
    payload = app.request.json
    with app.db.client() as session:
        spongebob = session.execute(select(User).filter_by(id=int(var))).scalar_one()
        spongebob.name = payload["name"]
        response = f"{spongebob}"
        session.commit()
        session.close()
    return response
