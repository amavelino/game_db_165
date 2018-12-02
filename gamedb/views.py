from django.shortcuts import render, redirect
from .models import Game
from .forms import CompanyForm, GameForm, CommentForm

# Create your views here.
def add_company(request):
	if request.method == "POST":
		form = CompanyForm(request.POST)
		if form.is_valid():
			company = form.save(commit=False)
			company.save()
	else:
		form = CompanyForm()
	return render(request, 'add.html', {'form':form, 'item': "Company"})
	
def add_game(request):
	if request.method == "POST":
		form = GameForm(request.POST)
		if form.is_valid():
			game = form.save(commit=False)
			game.save()
	else:
		form = GameForm()
	return render(request, 'add.html', {'form':form, 'item':"Game"})

def add_comment(request, gid):
	game = Game.objects.get(pk=gid)


	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.date_created = timezone.now()
			comment.date_last_edited = timezone.now()
			comment.gid = gid
			comment.save()
	else:
		form = CommentForm()
	return render(request, 'add.html', {'form':form, 'item':"Comment", 'game':game.title})

def show_games(request):
	items = Game.objects.all()
	return render(request, 'show-games.html', {'game_list':items})