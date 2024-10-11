from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pony.orm import db_session

from bank.models import User

from .auth.hash_password import HashPassword
from .auth.jwt_handler import create_access_token
from .models import TokenResponse, UserPydantic

user_route = APIRouter()

hash_password = HashPassword()


@user_route.post("/signup")
async def sign_user_up(
    first_name: str, last_name: str, password: str, email: str, phone: int
):
    user = UserPydantic(
        last_name=last_name,
        first_name=first_name,
        email=email,
        phone=phone,
        password=password,
    )
    with db_session:
        if User.get(email=email):
            return {"message": "account with this email already exists"}
        else:
            User(
                first_name=first_name,
                last_name=last_name,
                password=hash_password.create_hash(password),
                email=email,
                phone=phone,
            )
    return {"message": "account created"}


@user_route.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()):
    with db_session:
        user_exist = User.get(email=user.username)
        if user_exist and hash_password.verify_hash(user.password, user_exist.password):
            access_token = create_access_token(user_exist.email)
            return {"access_token": access_token, "token_type": "Bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
