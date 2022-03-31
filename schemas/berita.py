from pydantic import BaseModel

class Berita(BaseModel):
    title : str
    date : str
    author : str
    link : str
    category : str 
    website : str
    content : str


