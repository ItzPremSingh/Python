from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from .jwt_handler import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")


async def authenticate(token: str = Depends(oauth2_scheme)):
    if token:
        decoded_token = verify_access_token(token)
        return decoded_token["user"]

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="sign in for access"
    )
