import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import post, user, auth

from routers.database import engine
from routers import models

# to manage the ORM of models and database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS ( cross origin ressource sharing )
# https://fastapi.tiangolo.com/tutorial/cors/
origins = ["*"]

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
logger.info("initialize")

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello Heroku"}


