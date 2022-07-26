from fastapi import FastAPI
from routers import post

app = FastAPI()

# pourquoi utiliser un router?: to split pour une meilleure organisation?
app.include_router(post.router)

@app.get("/")
def root():
    return {"message": "Hello World"}




