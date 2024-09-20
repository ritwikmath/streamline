from core.application import Application
from bootstrap.bootstrap import Bootstrap


app = Application()
Bootstrap()

if __name__ == "__main__":
    app.handle("/simple/12", "GET")
