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


# TODO:
- requirements.txt for ease of installation in the future
- add more features ha ha