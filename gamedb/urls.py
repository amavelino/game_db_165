from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('company/add', views.add_company, name='add_company'),
	path('games/add', views.add_game, name='add_game'),
	path('games/', views.show_games, name='show_games'),
	path('games/<int:gid>/add-comment/', views.add_comment, name='add_comment'),
]