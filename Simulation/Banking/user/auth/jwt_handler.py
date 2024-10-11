from datetime import UTC, datetime
from time import time

from fastapi import HTTPException, status
from jose import JWTError, jwt

from common.setting import SECRET_TOKEN


def create_access_token(user: str) -> str:
    payload = {"user": user, "expires": time() + 3600}

    return jwt.encode(payload, SECRET_TOKEN, algorithm="HS256")


def verify_access_token(token: str) -> dict:
    try:
        data = jwt.decode(token, SECRET_TOKEN, algorithms=["HS256"])
        expire = data.get("expires")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="No token provided"
            )

        if datetime.now(UTC) > datetime.fromtimestamp(expire, UTC):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Token expired"
            )
        return data

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token"
        )
