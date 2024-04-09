from pydantic import BaseModel
from typing import Optional

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