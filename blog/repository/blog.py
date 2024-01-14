from fastapi import HTTPException, status
from .. import schemas, models
from sqlalchemy.orm import Session

def getAll(limit, offset, db: Session, sort, published):
    # return {'data': {'blogs': f'{limit} blogs at page {page}'}}
    blogs = db.query(models.Blog).limit(limit).offset(offset).all()
    return blogs

def create(blog: schemas.Blog, db: Session):
    newBlog = models.Blog(title=blog.title, body=blog.body)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog) # To get data after db insetion like the id generated by DB
    return newBlog

def destroy(id: int, db: Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, blog: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Blog with id {id} not found'
        )
    blog.update(blog)
    db.commit()
    return 'Updated'

def getOneById(id: int, db: Session):
    blog = db.query(models.Blog).where(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Blog with id {id} not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id {id} not found'}
    return blog