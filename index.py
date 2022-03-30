from fastapi import FastAPI
from routes.index import user
from routes.index import berita
app = FastAPI()

# app.include_router(user)
app.include_router(berita)