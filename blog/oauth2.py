

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import blog.token as token

_oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def getCurrentUser(userToken: str= Depends(_oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return token.verifyToken(userToken, credentials_exception)
    
    