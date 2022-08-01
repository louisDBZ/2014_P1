# How to run this project?

lien du tuto: https://www.youtube.com/watch?v=0sOvCWFmrtA&t=499s

#Database 


- télécharger postgre et pgadmin GUI

- aller sur pgadmin, entrer le mdp master et le mot de passe du user 'postgre'

https://www.postgresql.org/ftp/pgadmin/pgadmin4/v6.11/windows/

https://www.pgadmin.org/download/pgadmin-4-windows/

https://www.enterprisedb.com/postgresql-tutorial-resources-training?uuid=db55e32d-e9f0-4d7c-9aef-b17d01210704&campaignId=7012J000001NhszQAC

https://www.pgadmin.org/docs/pgadmin4/6.7/connect_to_server.html

problème: ne comprend pas pourquoi cela marche: après ré-installation et attente, soudainement ça a marché. 

# créer un env

pour mettre les codes de la db ( meme si écrit en clair dans mon code)

`py -3 -m venv venv`

edit configurations> Use specified interpreter

`venv\Scripts\activate`

pour créer le fichier gérant les variables d'environments:

(à la place de les ajouter une à une dans le gestionnaire de variables )

```
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

# le driver pour la bdd psycopg2

https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries

# API 

pour le lancer: télecharger uvicorn

lancer la commande depuis le dossier kindle-...

`uvicorn main:app --reload`

ou mieux aller sur postman

# plan de la database

une BDD avec user, password

et une ligne avec user, date et titre du livre


post excel file, manage exception
get statistcs de l'api
auth et user

# gestion de l'auth avec jwt/ Oauth2

`pip install python-jose[cryptography]`

commande pour générer arbitrairement la clé de l'algorithme, à mettre dans le .env:

`openssl rand -hex 32`

https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

pour décoder les jwt:

https://jwt.io/

# errors:

Error loading ASGI app. Could not import module "main".  => aller dans le dossier kindle


