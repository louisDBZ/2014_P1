from fastapi import FastAPI
from routers import post

# pour le lancer: télecharger uvicorn
# lancer la commande depuis le dossier kindle-...
# uvicorn main:app --reload
# ou mieux aller sur postman

app = FastAPI()

# pourquoi utiliser un router?
app.include_router(post.router)

@app.get("/")
def root():
    return {"message": "Hello World"}


