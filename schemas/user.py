from lib2to3.pytree import Base
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name : str
    email : str
    password : str
    
