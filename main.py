from fastapi import FastAPI
from blog.routers import user, blog, authentication
from blog import models
from blog.database import engine

# To Run this file "uvicorn blog.main:app --reload"
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)



