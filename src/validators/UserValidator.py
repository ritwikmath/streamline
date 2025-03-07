from pydantic import BaseModel


class UserValidator(BaseModel):
    name: str
    fullname: str

    class Config:
        from_attributes = True
