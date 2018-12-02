from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('add-company/', views.add_company, name='add_company')
]