from pydantic import BaseModel


class UserValidator(BaseModel):
    name: str
    fullname: str
