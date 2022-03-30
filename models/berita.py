from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import String
from config.db import meta

list_berita = Table(
    'berita', meta,
    Column('title',String(255)),
    Column('date',String(255)),
    Column('author',String(255)),
    Column('link',String(255)),
    Column('category',String(255)),
    Column('website',String(255))
)