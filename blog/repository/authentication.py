from fastapi import HTTPException, status

from blog import token
from .. import schemas, models
from sqlalchemy.orm import Session
from ..utils.hashing import Hash



def login(loginCreds: schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.email == loginCreds.username).first()
    if not user or not Hash.verify(user.password, loginCreds.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials")
    
    return token.createAccessToken({"sub": user.email})