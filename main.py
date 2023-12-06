from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.params import Body


class post(BaseModel):
    title: str
    content: str
    published: bool=True #default value is True
    rating: Optional[int] = None #making it optional and making default value as None

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/posts")
def create_posts(post: post):
    post_dict = post.dict()
    return post_dict