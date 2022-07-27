# How to run this project?

lien du tuto: https://www.youtube.com/watch?v=0sOvCWFmrtA&t=499s

#Database 

config 2:28:00

- télécharger postgre et pgadmin GUI

- aller sur pgadmin, entrer le mdp master et le mot de passe du user 'postgre'

https://www.postgresql.org/ftp/pgadmin/pgadmin4/v6.11/windows/

https://www.pgadmin.org/download/pgadmin-4-windows/

https://www.enterprisedb.com/postgresql-tutorial-resources-training?uuid=db55e32d-e9f0-4d7c-9aef-b17d01210704&campaignId=7012J000001NhszQAC

### documentations:
https://www.pgadmin.org/docs/pgadmin4/6.7/connect_to_server.html

problème: ne comprend pas pourquoi cela marche: après ré-installation et attente, soudainement ça a marché. 

# API 

pour le lancer: télecharger uvicorn
lancer la commande depuis le dossier kindle-...
uvicorn main:app --reload
ou mieux aller sur postman

# plan de la database

une BDD avec user, password
et une ligne avec user, date et titre du livre


post excel file, manage exception
get statistcs de l'api
auth et user



