"# game_db_165" 

Django 2.1.3
PostgreSQL 9.5.14

Database setup:

(In postgres:)

CREATE USER game_db_admin WITH PASSWORD 'game165dbpass';

CREATE DATABASE game_db_165 OWNER game_db_admin;

(Outside of postgres:)

python manage.py makemigrations

python manage.py migrate

python manage.py migrate --run-syncdb

# Current features:
- Sign up
- Log in and log out
- Create, read, update, and delete game entries
- Create, read, update, and delete comments (CUD functionality is only available for comments you made)
- Create, read, and update company entries
- Maybe more to come?

# For Heroku deployment:
see:

https://devcenter.heroku.com/articles/django-app-configuration

https://devcenter.heroku.com/articles/getting-started-with-python

- pip install gunicorn
- pip install django-heroku
- pip install whitenoise
- create Procfile
- create runtime.txt (indicates python version)
- create requirements.txt (use pip freeze > requirements.txt)
- edit settings.py (see the bottom of settings.py for edits made + add whitenoise to MIDDLEWARE)