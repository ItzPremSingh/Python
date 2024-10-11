from secrets import randbelow

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pony.orm import db_session

from .auth.authenticate import authenticate
from .auth.hash_password import HashPassword
from .auth.jwt_handler import create_access_token
from .model import Account, AccountPydantic, TokenResponse

accountRouter = APIRouter(prefix="/account/v1")
hash_password = HashPassword()


@accountRouter.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()):
    with db_session:
        user_exist = Account.get(email=user.username)
        if user_exist:
            if hash_password.verify_hash(user.password, user_exist.password):
                access_token = create_access_token(user_exist.email)
                return {"access_token": access_token, "token_type": "Bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@accountRouter.post("/create/")
async def createUser(name: str, password: str, email: str, phone: int):
    with db_session:
        if Account.get(name=name):
            return {"message": "account already exists"}

        else:
            Account(
                id=randbelow(1000),
                name=name,
                password=HashPassword().create_hash(password),
                email=email,
                phone=phone,
            )

    return {"message": "account created"}


@accountRouter.get("/login/")
async def loginUser():
    return {"message": "Login user"}


@accountRouter.get("/logout/")
async def logoutUser(user: str = Depends(authenticate)):
    print(user, type(user))
    return {"message": "Logout user"}


@accountRouter.get("/all/")
async def getAllUser():
    with db_session:
        return {
            "accounts": [AccountPydantic.model_validate(a) for a in Account.select()]
        }
