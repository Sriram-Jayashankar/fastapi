from fastapi import FastAPI,Response,Request,APIRouter
from pydantic import BaseModel
from typing import Optional
from fastapi.params import Body
import psycopg2
import time
from ..utils.schemas import Post
from ..utils.databse import connecttodb


# from ..main import conn,cursor
post=Post

router=APIRouter(tags=["POSTS"])

conn,cursor=connecttodb()

def convertListDict(list):
    keys=["id","title","content","published","rating"]
    final=[]
    for i in list:
        #print(dict(zip(keys,i)))
        final.append(dict(zip(keys,i)))
    return final

# @router.get("/")
# async def root():
#     return {"message": "Hello World"}
#create a post
@router.post("/posts")
def   create_posts(post: post):
    # print(type(post))
    post_dict = post.dict()
    # print(type(post_dict))
    cursor.execute("""select max(id) from posts""")
    value=cursor.fetchall()
    print(type(value[0][0]),value[0])
    post_dict["id"]=value[0][0]+1
    post_tuple= tuple(post_dict.values())
    print(post_tuple)
    cursor.execute("""insert into posts values(%s,%s,%s,%s,%s)""",post_tuple)
    # print(cursor.fetchone()[0])
    conn.commit()

    cursor.execute(""" select * from posts where id=%s""",(post_dict["id"],))
    temp=cursor.fetchone()
    print(type(temp),temp)

    #post_dict["id"]=len(posts)+1#creates a unique id for each post
    #posts.append(post_dict)
    return {"data":temp}

#read all posts
@router.get("/posts")
def get_all_posts():
    cursor.execute("""select * from posts""")
    post=cursor.fetchall()
    final=convertListDict(post)
    return {"data":final}

#read a single postjsjsj
@router.get("/posts/{id}")
def read_all_posts(id:int ):
    cursor.execute("""select * from posts where id=%s""",(id,))
    post=cursor.fetchall()
    print(type(post))
    return{"data":convertListDict(post)}


#write code for deleting particular post using the route /posts/{id} and the delete method

@router.delete("/posts/{id}")
def delete_post(id:int):
    cursor.execute("""delete from posts where id=%s""",(id,))
    conn.commit()
    return {"message":"post deleted successfully"}

#write code for updating particular post using the route /posts/{id} and the put method

@router.put("/posts/{id}")
def update_post(id:int,post:post):
    post_dict=post.dict()
    post_dict["id"]=id
    post_tuple=tuple(post_dict.values())
    #print(type(post))
    cursor.execute("""update posts set %s where id=%s""",(post_tuple,id))
    conn.commit()
    post_dict["id"]=id
    post=read_one_id(id)
    return {"message":"post updated successfully"}

#write code for updating particular post using the route /posts/{id} and the patch method
'''
@app.patch("/posts/{id}")
def update_post(id:int,post:post):
    post_dict=post.dict()
    post_dict["id"]=id
    post=read_one_id(id)
    if post==None:
        return Response(status_code=404)
    else:
        posts.remove(post)
        posts.append(post_dict)
        return {"message":"post updated successfully"}
'''
# @app.post("/testpost")
# async def testfun(hello:credentials):