from pydantic import BaseSettings

'''
on lui dit d'aller chercher dans .env les variables que l'on codait en dur dans le connect avant

le .env file est un fichier texte, il y a donc un cast à faire pour le type des variables d'environnments 
ces classes servent à cela

on a mis des valeurs par défault ici

host='localhost', port='5432',database='postgres', user='postgres', password='louis.debouzy'
'''

class Settings(BaseSettings):
    database_hostname: str ="localhost"
    database_port: str='5432'
    database_password: str
    database_name: str="postgres"
    database_username: str ="postgres"
    secret_key: str  # the hash key, used for the hashing
    algorithm: str='HS256'
    access_token_expire_minutes: int=60

    class Config:
        env_file = ".env"


settings = Settings()
# on crée une instance de setting qui va permettre de faire les validations
# et surtout permettre d'accéder aux variables depuis un autre fichier
