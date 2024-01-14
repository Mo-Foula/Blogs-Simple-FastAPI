from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List, Optional
from ..repository import user
from ..utils.hashing import Hash
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix='/user', tags=["Users"])

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(user= request, db= db)

@router.get('/', response_model=List[schemas.ShowUser])
def getAll(limit: int = 10, offset: int = 0, published: bool = True, sort: Optional[str] = None, db: Session = Depends(database.get_db)):
    return user.getAll(limit= limit, offset= offset, published= published, sort= sort, db=db)

@router.get('/{id}', response_model=schemas.ShowUser)
def getOneById(id: int, db: Session = Depends(database.get_db)):
    return user.getOneById(id, db)
