from fastapi import FastAPI,Response,Request
from pydantic import BaseModel
from typing import Optional
from fastapi.params import Body

posts=[{"title":"Blog 1", "content":"Content of Blog 1","id":1}, {"title":"Blog 2", "content":"Content of Blog 2","id":2}]#created a list of dictionaries to temporarily act as a database

#function to read an id of the post
def read_one_id(idvar):
    for i in posts:
        if i["id"] == idvar:
            return i
    return None


class post(BaseModel):
    title: str
    content: str
    published: bool=True #default value is True
    id: int
    rating: Optional[int] = None #making it optional and making default value as None

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
#create a post
@app.post("/posts")
def create_posts(post: post):
    post_dict = post.dict()
    post_dict["id"]=len(posts)+1#creates a unique id for each post
    posts.append(post_dict)
    return {"data":post_dict}

#read all posts
@app.get("/posts")
def get_all_posts():
    return {"data":posts}

#read a single post
@app.get("/posts/{id}")
def read_all_posts(id:int ):
    post=read_one_id(id)
    return{"data":post}


#write code for deleting particular post using the route /posts/{id} and the delete method

@app.delete("/posts/{id}")
def delete_post(id:int):
    post=read_one_id(id)
    if post==None:
        return Response(status_code=404)
    else:
        posts.remove(post)
        return {"message":"post deleted successfully"}



