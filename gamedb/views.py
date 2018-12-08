from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from .models import Game, Comment, Company
from django.contrib.auth.models import User

# --------------------------------------------------------- #
#							Sign up 						#
# --------------------------------------------------------- #
def signup(request):
	if request.method == "POST":
		username = request.POST['signup-username']
		password = request.POST['signup-password']
		email = request.POST['signup-email']

		user_obj = User.objects.create_user(username, email, password)

		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('home')
	form = None

	return render(request, 'signup.html', {'form':form})


# --------------------------------------------------------- #
#							Company 						#
# --------------------------------------------------------- #
@login_required
def add_company(request):
	active = "gamesCompanyAdd"
	return render(request, 'add-company.html', {'item': "Company", 'active': active})

@login_required
def add_company_action(request):
	active = "gamesCompanyAdd"
	if request.method == "POST":
		form = request.POST
		name = request.POST['companyName']
		desc = request.POST['companyDesedcription']
		new_company = Company(name=name, description=desc)
		new_company.save()
	form = None
	return render(request, 'add-company.html', {'form':form, 'item': "Company", 'active': active, 'success': 1})

def show_company(request):
	active = "gamesCompanyList"
	items = Company.objects.all()
	return render(request, 'show-company.html', {'comp_list':items, 'active': active})

@login_required
def edit_company(request, compid):
	company_obj = Company.objects.get(pk=compid)
	
	company_details = {}
	company_details['compid'] = company_obj.compid
	company_details['name'] = company_obj.name
	company_details['description'] = company_obj.description

	form = QueryDict('', mutable=True)
	form.update(company_details)

	return render(request, 'edit-company.html', {'form':form, 'item': "Company"})

@login_required
def edit_company_action(request, compid):
	if request.method == "POST":
		form = request.POST
		form._mutable = True
		name = request.POST['companyName']
		desc = request.POST['companyDescription']

		company_obj = Company.objects.filter(pk=compid)
		company_obj.update(name=name, description=desc)
		form.update(compid=compid, name=name, description=desc)

	return render(request, 'edit-company.html', {'form':form, 'item': "Company", 'success':1})

# --------------------------------------------------------- #
#							Game 	 						#
# --------------------------------------------------------- #
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
	return render(request, 'add-game.html', {'form':form, 'item':"Game", 'active': active, 'success': 1})

def show_games(request):
	active = "gamesList"
	items = Game.objects.all()
	items = items.order_by('title')

	return render(request, 'show-games.html', {'game_list':items, 'active': active})

def show_game_info(request, gid):
	game = Game.objects.get(pk=gid)
	comments = Comment.objects.filter(gid=gid)

	user_comment = Comment.objects.filter(gid=gid, made_by=request.user)

	comment_details = {}
	if user_comment:
		comment_details['comment'] = user_comment[0].content
		comment_details['rating'] = user_comment[0].rating
		comment_details['commid'] = user_comment[0].commid
		comment_details['exists'] = 1
	else:
		comment_details['rating'] = 3
	form = QueryDict('', mutable=True)
	form.update(comment_details)

	return render(request, 'show-game-info.html', {'game':game, 'comments':comments, 'form': form})

@login_required
def edit_game(request, gid):
	game_obj = Game.objects.get(pk=gid)

	game_details = {}
	game_details['gid'] = game_obj.gid
	game_details['title'] = game_obj.title
	game_details['game_type'] = game_obj.game_type
	game_details['release_date'] = game_obj.release_date
	game_details['description'] = game_obj.description
	game_details['made_by'] = game_obj.made_by

	form = QueryDict('', mutable=True)
	form.update(game_details)

	return render(request, 'edit-game.html', {'form': form, 'item':"Game"})

@login_required
def edit_game_action(request, gid):
	if request.method == "POST":
		form = request.POST
		form._mutable = True
		form.update(gid=gid)
		title = request.POST['title']
		game_type = request.POST['game_type']
		release_date = request.POST['release_date']
		description = request.POST['description']
		made_by = get_company(request.POST['made_by'])

		game_obj = Game.objects.filter(gid=gid)
		game_obj.update(title=title, game_type=game_type, release_date=release_date, description=description, made_by=made_by)
	return render(request, 'edit-game.html', {'form': form, 'item':"Game", 'success': 1})

@login_required
def delete_game(request, gid):
	game_obj = Game.objects.get(pk=gid).delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# --------------------------------------------------------- #
#							Comment 						#
# --------------------------------------------------------- #
@login_required
def save_comment(request, gid):
	game = Game.objects.get(pk=gid)

	if request.method == "POST":
		form = request.POST
		content = request.POST['comment']
		rating = request.POST['rating']
		gid = game
		date_created = timezone.now()
		date_last_edited = timezone.now()
		made_by = request.user

		user_comment = Comment.objects.filter(made_by=made_by, gid=game)

		if user_comment:
			user_comment.update(content=content,rating=rating, date_last_edited=date_last_edited)
		else:
			new_comment = Comment(gid=gid, content=content, rating=rating, date_created=date_created, date_last_edited=date_last_edited, made_by=made_by)
			new_comment.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_comment(request, gid, commid):
	comment_obj = Comment.objects.get(pk=commid)

	if comment_obj.made_by == request.user:
		comment_obj.delete()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))