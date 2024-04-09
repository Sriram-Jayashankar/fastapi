from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    id :Optional[str]=-1
    title: str
    content: str
    published: bool=True #default value is True
    # id: int
    rating: Optional[int] = None #making it optional and making default value as None


class User(BaseModel):
    id:Optional[int]
    email:str
    password:str
    name:str