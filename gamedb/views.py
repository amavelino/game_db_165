from django.shortcuts import render, redirect
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

def add_comment(request):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.save()
	else:
		form = CommentForm()
	return render(request, 'add.html', {'form':form, 'item':"Comment"})