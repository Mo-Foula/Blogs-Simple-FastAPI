from typing import List, Optional
from pydantic import BaseModel
# Pydantic model is called schema whileas SQLAlchemy model is called model
# Pydantic is a simple data validation and manipulation package
# SQLAlchemy is obviously an ORM
class BlogBase(BaseModel):
    title: str
    body: str
    # published: Optional[bool] This line doesn't work in SQLAlchemy orm mapping (Show Blog class crashes on endpoint call)
    
class Blog(BlogBase):
    class Config():
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogBase] = []
    class Config():
        from_attributes = True # Instead of orm_mode

class ShowBlogTitleOnly(BaseModel):
    title: str
    class Config():
        from_attributes = True # Instead of orm_mode


        
# Pydantic models can be created from arbitrary class instances to support models that map to ORM objects.
class ShowBlog(Blog):
    # pass
    # class Config:
    #     orm_mode = True
    title: str
    body: str
    creator: ShowUser | None
    class Config():
        from_attributes = True 

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None