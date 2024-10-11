from pony.orm import PrimaryKey, Required, Set
from pydantic import BaseModel

from common import DB


class Account(DB.Entity):
    id = PrimaryKey(int)
    name = Required(str)
    password = Required(str)
    email = Required(str)
    phone = Required(int)
    houses = Set("House", reverse="owner")

    def __str__(self):
        return self.name


class AccountPydantic(BaseModel):
    id: int
    name: str
    password: str
    email: str
    phone: int

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
