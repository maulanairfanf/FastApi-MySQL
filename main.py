from fastapi import FastAPI
# from routes.index import berita
app = FastAPI()

# app.include_router(berita)

@app.get("/")
def home():
    return {"message":"Hello World"}