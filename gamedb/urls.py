from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('add-company/', views.add_company, name='add_company'),
	path('add-game/', views.add_game, name='add_game'),
	path('add-comment/', views.add_comment, name='add_comment'),
]