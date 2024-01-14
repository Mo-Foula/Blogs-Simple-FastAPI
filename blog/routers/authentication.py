from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database
from ..repository import authentication
from sqlalchemy.orm import Session
from blog import schemas

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db) ):
    return authentication.login(loginCreds= request, db=db)