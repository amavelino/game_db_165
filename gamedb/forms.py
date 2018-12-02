from django.forms import ModelForm
from .models import Company, Game, Comment


class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = ['name', 'description']

class GameForm(ModelForm):
	class Meta:
		model = Game
		fields = ['title', 'game_type', 'release_date', 'description', 'made_by']

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['content', 'rating']
