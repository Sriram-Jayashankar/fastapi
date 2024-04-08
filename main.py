from fastapi import FastAPI,Response,Request
from pydantic import BaseModel
from typing import Optional
from fastapi.params import Body
import psycopg2
import time
posts=[{"title":"Blog 1", "content":"Content of Blog 1","id":1},{"title":"Blog 2", "content":"Content of Blog 2","id":2}]#created a list of dictionaries to temporarily act as a database





# connecting to postgres database


# to ensure that it connects and if thres any issue put that onto the screen we use a while loop and a time.sleep function
while(True):
    try:
        conn=psycopg2.connect("dbname=fastapiDatabase user=postgres password=builafisory")
        break
    except Exception as e:
        print(f"error while connecting\n{e}")
    time.sleep(5)

cursor=conn.cursor()
cursor.execute("""select * from posts""")
records=cursor.fetchall()
print(records)
#function to read an id of the post
def read_one_id(idvar):
    for i in posts:
        if i["id"] == idvar:
            return i
    return None

#if i make something optional i need to give it a default value because there is no id in the body of the request it ,and i add it later 
class post(BaseModel):
    id :Optional[str]=-1
    title: str
    content: str
    published: bool=True #default value is True
    # id: int
    rating: Optional[int] = None #making it optional and making default value as None


class credentials(BaseModel):
    email:str
    password:str
    phoneno: int
    name:Optional[str]

app=FastAPI()

def convertListDict(list):
    keys=["id","title","content","published","rating"]
    final=[]
    for i in list:
        #print(dict(zip(keys,i)))
        final.append(dict(zip(keys,i)))
    return final

@app.get("/")
async def root():
    return {"message": "Hello World"}
#create a post
@app.post("/posts")
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
@app.get("/posts")
def get_all_posts():
    cursor.execute("""select * from posts""")
    post=cursor.fetchall()
    final=convertListDict(post)
    return {"data":final}

#read a single postjsjsj
@app.get("/posts/{id}")
def read_all_posts(id:int ):
    cursor.execute("""select * from posts where id=%s""",(id,))
    post=cursor.fetchall()
    print(type(post))
    return{"data":convertListDict(post)}


#write code for deleting particular post using the route /posts/{id} and the delete method

@app.delete("/posts/{id}")
def delete_post(id:int):
    cursor.execute("""delete from posts where id=%s""",(id,))
    conn.commit()
    return {"message":"post deleted successfully"}

#write code for updating particular post using the route /posts/{id} and the put method

@app.put("/posts/{id}")
def update_post(id:int,post:post):
    post_dict=post.dict()
    post_tuple=tuple(post.values())
    cursor.execute("""update posts set %s where id=%s""",(id,))
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
#     return {"data":hello}

@app.post("/testpost")
async def testfun(request: Request):
    try:
        json= await request.json()
        return {"data":json}
    except(e):
        return{"erdggdgror":e}
