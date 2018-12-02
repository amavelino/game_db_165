from django.db import models

# Create your models here.
class User_acct(models.Model):
	uid =				models.AutoField(primary_key=True, unique=True)
	username = 			models.CharField(max_length=30)
	# integrate with built-in django users ??

class Company(models.Model):
	compid = 			models.AutoField(primary_key=True, unique=True)
	name = 				models.CharField(max_length=100)
	description = 		models.TextField()

	def __str__(self):
		return self.name
	class Meta:
		managed = True
		db_table = 'company'

class Game(models.Model):
	gid = 				models.AutoField(primary_key=True, unique=True)
	title = 			models.TextField()
	game_type = 		models.TextField()
	release_date = 		models.DateField()
	description = 		models.TextField()
	made_by = 			models.ForeignKey(Company, on_delete=models.SET_NULL, db_column='name', null=True)

	def __str__(self):
		return self.gid
	class Meta:
		managed = True
		db_table = 'game'
		#unique_together = ()

class Comment(models.Model):
	commid = 			models.AutoField(primary_key=True, unique=True)
	gid =				models.ForeignKey(Game, on_delete=models.CASCADE, db_column='gid')
	content = 			models.CharField(max_length=500)
	rating = 			models.IntegerField()#min_value=1, max_value=5)
	date_created = 		models.DateField()
	date_last_edited = 	models.DateField()

	def __str__(self):
		return self.commid
	class Meta:
		managed = True
		db_table = 'comment'
		#unique_together = ()

class Platform(models.Model):
	pname = 			models.TextField(primary_key=True, unique=True)
	description = 		models.TextField()

	def __str__(self):
		return self.pname
	class Meta:
		managed = True
		db_table = 'platform'

class Genre(models.Model):
	gname = 			models.TextField(primary_key=True, unique=True)
	description = 		models.TextField()

	def __str__(self):
		return self.gname
	class Meta:
		managed = True
		db_table = 'genre'