from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from .models import Game, Comment, Company
from .forms import CompanyForm, GameForm, CommentForm

@login_required
def add_company(request):
	if request.method == "POST":
		form = CompanyForm(request.POST)
		if form.is_valid():
			company = form.save(commit=False)
			company.save()
	else:
		form = CompanyForm()
	return render(request, 'add.html', {'form':form, 'item': "Company"})

def show_company(request):
	items = Company.objects.all()
	return render(request, 'show-company.html', {'comp_list':items})

@login_required
def edit_company(request, compid):
	company_obj = Company.objects.get(pk=compid)

	if request.method == "POST":
		form = CompanyForm(request.POST, instance=company_obj)
		if form.is_valid():
			company = form.save(commit=False)
			company.save()
	else:
		form = CompanyForm(instance=company_obj)
	return render(request, 'edit.html', {'form':form, 'item': "Company"})




@login_required
def add_game(request):
	if request.method == "POST":
		form = GameForm(request.POST)
		if form.is_valid():
			game = form.save(commit=False)
			game.save()
	else:
		form = GameForm()
	return render(request, 'add.html', {'form':form, 'item':"Game"})

def show_games(request):
	items = Game.objects.all()
	return render(request, 'show-games.html', {'game_list':items})

def show_game_info(request, gid):
	game = Game.objects.get(pk=gid)
	comments = Comment.objects.filter(gid=gid)

	return render(request, 'show-game-info.html', {'game':game, 'comments':comments})

@login_required
def edit_game(request, gid):
	game_obj = Game.objects.get(pk=gid)

	if request.method == "POST":
		form = GameForm(request.POST, instance=game_obj)
		if form.is_valid():
			game = form.save(commit=False)
			game.save()
	else:
		form = GameForm(instance=game_obj)
	return render(request, 'edit.html', {'form': form, 'item':"Game"})

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

@login_required
def edit_comment(request, gid, commid):
	game = Game.objects.get(pk=gid)
	comment_obj = Comment.objects.get(pk=commid)

	if request.method == "POST":
		form = CommentForm(request.POST, instance=comment_obj)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.date_last_edited = timezone.now()
			comment.gid = game
			comment.save()
	else:
		form = CommentForm(instance=comment_obj)
	return render(request, 'edit.html', {'form':form, 'item':"Comment", 'game':game.title})