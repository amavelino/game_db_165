"# game_db_165" 

Django 2.1.3
PostgreSQL 9.5.14

Setup:
pip install django
pip install psycopg2

Database setup:
CREATE USER game_db_admin WITH PASSWORD 'game165dbpass';
CREATE DATABASE game_db_165 OWNER game_db_admin;

...

python manage.py migrate


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