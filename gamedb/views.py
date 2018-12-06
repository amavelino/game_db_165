from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from .models import Game, Comment
from .forms import CompanyForm, GameForm, CommentForm

@login_required
def add_company(request):
	active_item = "gamesCompanyAdd"
	if request.method == "POST":
		form = CompanyForm(request.POST)
		if form.is_valid():
			company = form.save(commit=False)
			company.save()
	else:
		form = CompanyForm()
	return render(request, 'add.html', {'form':form, 'item': "Company", 'active': active_item})

@login_required
def add_game(request):
	active_item = "gamesAdd"
	if request.method == "POST":
		form = GameForm(request.POST)
		if form.is_valid():
			game = form.save(commit=False)
			game.save()
	else:
		form = GameForm()
	return render(request, 'add.html', {'form':form, 'item':"Game", 'active' : active_item})

@login_required
def add_comment(request, gid):
	game = Game.objects.get(pk=gid)

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.date_created = timezone.now()
			comment.date_last_edited = timezone.now()
			comment.gid = game
			comment.save()
	else:
		form = CommentForm()
	return render(request, 'add.html', {'form':form, 'item':"Comment", 'game':game.title})

def show_games(request):
	active_item = "gamesList"
	items = Game.objects.all()
	return render(request, 'show-games.html', {'game_list':items, 'active' : active_item})

def show_game_info(request, gid):
	game = Game.objects.get(pk=gid)
	comments = Comment.objects.filter(gid=gid)

	return render(request, 'show-game-info.html', {'game':game, 'comments':comments})