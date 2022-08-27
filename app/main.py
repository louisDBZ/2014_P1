import pytest
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import post, user, auth
# comprendre pourquoi heroku il faut un point et pour pytest par exemple, il ne faut pas de point
# idem le setting le .env


from routers.database import engine
from routers import models


models.Base.metadata.create_all(bind=engine) # cette ligne sert à gérer l'ORM de models et database

app = FastAPI()

# pour lutter contre les problèmes de CORS ( cross origin ressource sharing )
# https://fastapi.tiangolo.com/tutorial/cors/
origins = ["*"] # normalement, ici on liste les adresses qui nous interessent

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#create a logger
logger = logging.getLogger()
#set logger level
logger.setLevel(logging.INFO)

handler = logging.FileHandler('logfile.log')
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("initialize") # et pas logging!

# pourquoi utiliser un router?: to split pour une meilleure organisation?
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# se poser la question du choix de la faire asynchrone ou non
@app.get("/")
def root():
    return {"message": "Hello Heroku"}


