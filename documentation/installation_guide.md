# Sovelluksen asennusohje

Kloonaa tämä repositorio koneellesi ja mene repositorion juureen. Suorita seuraavat komennot järjestyksessä:

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

Nyt sovellus on käyttövalmis. Käynnistä sovellus komennolla `python3 run.py`

Herokuun sovelluksen saa pyörimään seuraavilla komennoilla (venv aktivoituna):

1. `pip install gunicorn`
2. `pip freeze | grep -v pkg-resources > requirements.txt`
3. `echo "web: gunicorn --preload --workers 1 application:app" > Procfile`
4. `heroku create projektin_nimi`
5. `git remote add heroku https://git.heroku.com/projektin_nimi.git`
6. `git add .`
7. `git commit -m "Initial commit"`
8. `git push heroku master`
