from fastapi import FastAPI,Response,Request
from pydantic import BaseModel
from typing import Optional
from fastapi.params import Body
import psycopg2
import time
from .routes import posts,user
# posts=[{"title":"Blog 1", "content":"Content of Blog 1","id":1},{"title":"Blog 2", "content":"Content of Blog 2","id":2}]#created a list of dictionaries to temporarily act as a database





# connecting to postgres database


# to ensure that it connects and if thres any issue put that onto the screen we use a while loop and a time.sleep function


    
# cursor.execute("""select * from posts""")
# records=cursor.fetchall()
# print(records)
#function to read an id of the post

#if i make something optional i need to give it a default value because there is no id in the body of the request it ,and i add it later 


conn,cursor=connecttodb()
app=FastAPI()
app.include_router(posts.router)
app.include_router(user.router)

    # app.include_router(user.APIRouter)

