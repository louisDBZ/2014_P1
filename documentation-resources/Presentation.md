# Problématique:

1- Amazon Kindle fourni nos notes sous forme d'un csv ou bien un pdf,ce n'est pas pratique pour relire ses notes -

Actuellement, je fais un copier coller de chaque ligne du pdf dans un Microsoft word

Je cherche à l'automatiser

![img.png](kindle_note.jpg)

The convention is this one:

put your notes and highlighted texts in the return file

if your note is tagged with @@something,
the note and the hightlited texts will be added to another file, then you will have this other file 

thepath of the file is parametered  thanks to the file_mapper.json file, that you should also provide


Meaning that I will store for every person a folder with some data? plutot que de le mettre dans un autre fichier,
le mettre dans le meme mais à la suite, en dessous..


# possible improvments:

2- La gestion des photos sur Kindle est compliquée : à tel point que je prend en photo mon kindle 

# Architecture logicielle

![img.png](SW_architecture_diagram.png)

to do: changer chrome par postman

pourquoi psycopg et sql alchemy? car besoin de connaitre les id  de la BDD en read-only


# Architecture des données

### table "posts"

- post_id Integer, primary_key

- title String

- post_created_at TIMESTAMP

- user_id Integer ForeignKey

### table "users"

- user_id Integer primary_key

- email String

- password String

- user_created_at TIMESTAMP


# Fonctionalités 

to do: le mettre en diagramme UML

- post excel file
- auth et user

![img.png](FastAPI-screenshot.JPG)
