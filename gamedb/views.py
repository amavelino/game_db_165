from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from .models import Game, Comment, Company
from .forms import CompanyForm, GameForm, CommentForm

@login_required
def add_company(request):
	active = "gamesCompanyAdd"
	if request.method == "POST":
		form = CompanyForm(request.POST)
		if form.is_valid():
			company = form.save(commit=False)
			company.save()
	else:
		form = CompanyForm()
	return render(request, 'add.html', {'form':form, 'item': "Company", 'active': active})

def show_company(request):
	active = "gamesCompanyList"
	items = Company.objects.all()
	return render(request, 'show-company.html', {'comp_list':items, 'active': active})

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
	active = "gamesAdd"
	default_data={'release_date': timezone.now()}
	querydict_defdata = QueryDict('', mutable=True)
	querydict_defdata.update(default_data)
	return render(request, 'add-game.html', {'form': querydict_defdata, 'item':"Game", 'active': active})

def get_company(company):
	existing_company = Company.objects.filter(name=company)
	if len(existing_company)==0:
		new_comp = Company(name=company, description="No Descriptions Added")
		new_comp.save()
	return Company.objects.get(name=company)

def add_game_action(request):
	active = "gamesAdd"
	if request.method == "POST":
		form = request.POST
		title = request.POST['gameTitle']
		game_type = request.POST['game_type']
		release_date = request.POST['release_date']
		description = request.POST['description']
		made_by = get_company(request.POST['made_by'])

		new_game = Game(title=title, game_type=game_type, release_date=release_date, description=description, made_by=made_by)
		new_game.save()
	form = None
	return render(request, 'add-game.html', {'form':form, 'item':"Game", 'active': active})

def show_games(request):
	active = "gamesList"
	items = Game.objects.all()
	return render(request, 'show-games.html', {'game_list':items, 'active': active})

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