#dockerfile
# le python est le nom de l'image docker, pas la version de python qu'on utilise
FROM python:3.9.7
# sur le container, on s'est assuré qu'il existait un folder usr/src/ dans lequel on a mis notre app
WORKDIR /usr/src/kindle-note-caster-api
# mettre ./ revient à dire tu le copies dans le dossier /usr/src/app
COPY requirements.txt ./
# important de mettre no cache car sinon les modifs ne sont pas prises en compte
RUN pip install --no-cache-dir -r requirements.txt
# idem pour le second point
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]