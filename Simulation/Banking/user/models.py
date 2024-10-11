from re import search

from pony.orm import PrimaryKey, Required
from pydantic import BaseModel, field_validator
from pydantic_core import ValidationError

from common import DB


class User(DB.Entity):
    first_name = Required(str, sql_type="VARCHAR(20)", max_len=20)
    last_name = Required(str, sql_type="VARCHAR(20)", max_len=20)
    password = Required(str, sql_type="VARCHAR(16)")
    email = PrimaryKey(str, sql_type="VARCHAR(30)")
    phone = Required(int, sql_type="VARCHAR(10)", unique=True)

    def __str__(self):
        return self.email


class UserPydantic(BaseModel):
    first_name: str
    last_name: str
    password: str
    email: str
    phone: int

    @field_validator("email")
    def email_validator(cls, v: str):
        if not search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,}$", v.lower()):
            raise ValidationError("Invalid email address")
        return v.lower()

    @field_validator("phone")
    def phone_validator(cls, v: int):
        if not search(r"^[6-9]\d{9}$", str(v)):
            raise ValidationError("Invalid phone number")

        return v

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
