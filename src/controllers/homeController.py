from core.application import app
from sqlalchemy import select
from database.models.userAccount import User

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