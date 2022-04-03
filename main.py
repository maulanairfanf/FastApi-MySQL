from fastapi import FastAPI
from routes.index import berita
app = FastAPI()

app.include_router(berita)

# @app.get("/")
# async def root():
#     return {"message" : "Hello from world"}