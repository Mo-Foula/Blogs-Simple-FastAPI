
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from blog import models, schemas
from blog.utils.hashing import Hash


def getOneById(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} was not found")
    return user

def getAll(limit: int, offset: int, published: bool, sort: Optional[str], db: Session):
    users = db.query(models.User).limit(limit).offset(offset).all()
    return users

def create(user: schemas.User, db: Session):
    hashedPassword = Hash.bcrypt(user.password)
    newUser = models.User(name = user.name, email = user.email, password= hashedPassword)
    db.add(newUser)
    db.commit()
    db.refresh(newUser) # To get data after db insetion like the id generated by DB
    return newUser