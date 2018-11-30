from django.db import models

# Create your models here.
class User_acct(models.Model):
	uid =				models.IntegerField(primary_key=True, unique=True)
	username = 			models.CharField(max_length=30)
	# integrate with built-in django users

class Company(models.Model):
	compid = 			models.IntegerField(primary_key=True, unique=True)
	name = 				models.CharField(max_length=100)
	description = 		models.TextField()

class Game(models.Model):
	gid = 				models.IntegerField(primary_key=True, unique=True)
	title = 			models.TextField()
	game_type = 		models.TextField()
	release_date = 		models.DateField()
	description = 		models.TextField()

class Comment(models.Model):
	commid = 			models.
	gid =				models.ForeignKey(Game, )
	content = 			models.CharField(max_length=500)
	rating = 			models.
	date_created = 		models.DateField()
	date_last_edited = 	models.DateField()

class Platform(models.Model):
	pname = 			models.TextField(primary_key=True, unique=True)
	description = 		models.TextField()

class Genre(models.Model):
	gname = 			models.TextField(primary_key=True, unique=True)
	description = 		models.TextField()