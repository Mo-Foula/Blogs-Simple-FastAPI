from fastapi import APIRouter, Depends, Response, status
from typing import List, Optional

from blog.oauth2 import getCurrentUser
from .. import schemas, database
from ..repository import blog
from sqlalchemy.orm import Session

router = APIRouter(prefix='/blog', tags=["Blogs"])

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def getOneById(id: int, response: Response, db: Session = Depends(database.get_db)):
    return blog.getById(id, db)

@router.get('/', response_model=List[schemas.ShowBlog])
def getAll(limit: int = 10, offset: int = 0, published: bool = True, sort: Optional[str] = None, db: Session = Depends(database.get_db), getCurrentUser: schemas.User = Depends(getCurrentUser)):
    return blog.getAll(limit=limit, offset=offset, db=db, sort=sort, published=published)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(blog= request, db= db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(database.get_db)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(request: schemas.Blog, db: Session = Depends(database.get_db)):
    # {'title' : request.title,'body' : request.body}
    return blog.update(id, blog= request, db= db)


# @router.get('/{id}/comments')
# def getBlogCommentsById(id: int, limit: int = 10, page: int = 1):
#     return {'data': {id: id, 'comments': ["Yess", "Noo"]}}

# @router.get('/unpublished')
# def getBlogsUnpublished():
#     return {'data': {'blogs': ["Madinaty", "Madinaty Nasry"]}}
