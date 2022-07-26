from fastapi import FastAPI

# pour le lancer: télecharger uvicorn et lancer la commande
#uvicorn main:app --reload

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
