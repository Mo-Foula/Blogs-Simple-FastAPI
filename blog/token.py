from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from blog.schemas import Token, TokenData

_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
_ALGORITHM = "HS256"
_ACCESS_TOKEN_EXPIRE_MINUTES = 30


def _createAccessToken(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=_ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, _SECRET_KEY, algorithm=_ALGORITHM)
    return encoded_jwt


def createAccessToken(data: dict):
    access_token = _createAccessToken(data=data)
    return Token(access_token=access_token, token_type="bearer")

def verifyToken(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, _SECRET_KEY, algorithms=[_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception

