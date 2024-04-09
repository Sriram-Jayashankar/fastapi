from fastapi import APIRouter
from ..utils.schemas import User

userclass=User

router=APIRouter

@router.post("/user")
def create_user(user:userclass):
    user_dict=user.dict()
    cursor.execute("""select max(id) from usertable""")
    temp=cursor.fetchone()
    print(temp)
    return