# How to run this project?

lien du tuto: https://www.youtube.com/watch?v=0sOvCWFmrtA&t=499s

#Database 


- télécharger postgre et pgadmin GUI

- aller sur pgadmin, entrer le mdp master et le mot de passe du user 'postgre'

- aller sur Schemas>Public>Table

https://www.postgresql.org/ftp/pgadmin/pgadmin4/v6.11/windows/

https://www.pgadmin.org/download/pgadmin-4-windows/

https://www.enterprisedb.com/postgresql-tutorial-resources-training?uuid=db55e32d-e9f0-4d7c-9aef-b17d01210704&campaignId=7012J000001NhszQAC

https://www.pgadmin.org/docs/pgadmin4/6.7/connect_to_server.html

problème: ne comprend pas pourquoi cela marche: après ré-installation et attente, soudainement ça a marché. 

# créer un env

pour mettre les codes de la db ( meme si écrit en clair dans mon code)

`py -3 -m venv venv`  le second venv est le nom que l'on a donné à l'environment

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

# l'ORM ( Ogject relational Mapper): sqlachelmy

`pip install sqlalchemy`

# pydantic

`pip install pydantic[dotenv]`

`pip install pydantic[email]`

# API 

 télecharger uvicorn

`pip install uvicorn`

https://fastapi.tiangolo.com/deployment/manually/

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

# passlib

`pip install passlib`

# ?

`pip install python-multipart`

`pip install python-docx`

`pip install pandas` voir les versions au plus clair: 1.2.4 ou 1.4.3?

# documentation

disponible à l'adresse: http://127.0.0.1:8000/docs


# exemple pour la config du file_mapper.json
```json
{
"marketing": "Lecture/Marketing.docx",
"sales": "Lecture/Sales.docx"
}
```

# TO DO:

## MUST HAVE

- Deploy to docker (section 15)

- Automatic tests with pytests ( section 16) 

- faire un clean la doc fastapi

## NICE TO HAVE

-gestion des print et des logging

https://pythonexamples.org/python-logging-info/

- remettre de l'ordre dans mes terminaux, ou les imports se font

- remettre de l'ordre dans mes imports entre les dossiers, et lire:

https://iq-inc.com/importerror-attempted-relative-import/

- terminer la relecture de mes notes

- faire la page web qui appelle ce service

https://stackoverflow.com/questions/64168340/how-to-send-a-file-docx-doc-pdf-or-json-to-fastapi-and-predict-on-it-without

- à creuser: bel affichage d'un dataframe dans un terminal intelliji 

- transfomer ces print en console.log

- refaire le git ignore de Lecture

- la db semble avoir un pb au démarrage, reloading de la db

- faire un fstring pour apprendre

- recorriger les doctypes
