from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import String,Text
from config.db import meta

list_berita = Table(
    'berita', meta,
    Column('title',String()),
    Column('date',String()),
    Column('author',String()),
    Column('link',String()),
    Column('category',String()),
    Column('website',String()),
    Column('content',String())
)