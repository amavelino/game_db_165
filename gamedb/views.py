from django.shortcuts import render, redirect
from .forms import CompanyForm

# Create your views here.
def add_company(request):
	if request.method == "POST":
		form = CompanyForm(request.POST)
		if form.is_valid():
			company = form.save(commit=False)
			company.save()
	else:
		form = CompanyForm()
	return render(request, 'add-company.html', {'form':form})