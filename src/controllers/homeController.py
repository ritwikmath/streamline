from core.application import app
from sqlalchemy import select
from database.models.userAccount import User
from sqlalchemy import update


@app.router.get('/simple/{var}')
def simple(var):
    with app.db.client() as session:
        spongebob = User(
            name="spongebob",
            fullname="Spongebob Squarepants",
        )
        session.add(spongebob)
        query = select(User)
        for user in session.scalars(query):
            app.logger.info(user)
        session.commit()
        session.close()
    app.cache.store_value("surname", "math")
    app.logger.info(app.cache.get_value("surname"))
    app.logger.info(var)
    return 'result from the fn'


@app.router.post('/simple')
def simple_store(payload):
    with app.db.client() as session:
        spongebob = User(**payload)
        session.add(spongebob)
        query = select(User)
        for user in session.scalars(query):
            app.logger.info(user)
        response = f"{spongebob}"
        print(response)
        session.commit()
        session.close()
    return response


@app.router.patch('/simple/{var}')
def simple_update(var):
    payload = app.request.json
    with app.db.client() as session:
        spongebob = session.execute(select(User).filter_by(id=int(var))).scalar_one()
        spongebob.name = payload["name"]
        response = f"{spongebob}"
        print(response)
        session.commit()
        session.close()
    return response
