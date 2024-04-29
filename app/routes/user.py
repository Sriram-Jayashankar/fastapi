from fastapi import APIRouter
from ..utils.schemas import User
from ..utils.databse import connecttodb

# from ..main import conn,cursor

userclass=User
conn,cursor=connecttodb()
router=APIRouter()

@router.post("/user")
def create_user(user:userclass):
    user_dict=user.dict()
    cursor.execute("""select max(id) from userstable""")
    tempid=cursor.fetchone()
    users_tuple=tuple(user_dict.values())
    user_dict["id"]=tempid[0]+1
    cursor.execute("""insert into userstable(id,email,password,name,user_id) values(%s,%s,%s,%s,%s)""",(users_tuple))
    conn.commit()
    cursor.execute("select * from userstable where id=%s",(tempid,))
    var=cursor.fetchone()
    return {"data":var}