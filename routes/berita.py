from unicodedata import category
from fastapi import APIRouter
from config.db import conn
from models.index import list_berita
from schemas.index import Berita

berita = APIRouter()

@berita.get("/")
async def read_data():
    return conn.execute(list_berita.select()).fetchall()

@berita.get("/category/{category}")
async def filter_category(category : str):
    return conn.execute(list_berita.select().where(list_berita.c.category == category)).fetchall()

@berita.get("/website/{website}")
async def filter_website(website : str):
    return conn.execute(list_berita.select().where(list_berita.c.website == website)).fetchall()

@berita.get("/date/{date}")
async def filter_date(date : str):
    return conn.execute(list_berita.select().where(list_berita.c.date == date)).fetchall()