from core.application import Application
from bootstrap.bootstrap import Bootstrap


app = Application()
Bootstrap()

if __name__ == "__main__":
    app.handle("/simple/5", "GET")
    # payload = {
    #     "name": "SpongeBob",
    #     "full_name": "SpongeBob SquarePants"
    # }
    # app.handle("/simple", "POST", payload=payload)
    # payload = {
    #     "name": "Sponge Bob"
    # }
    # app.handle("/simple/5", "PATCH", payload=payload)
