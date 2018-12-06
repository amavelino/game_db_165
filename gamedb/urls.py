from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('company/add/', views.add_company, name='add_company'),
	path('company/', views.show_company, name='show_company'),
	#path('company/<int:compid>', views.show_company_info, name='show_company_info'),
	path('company/<int:compid>/edit/', views.edit_company, name='edit_company'),

	path('games/add/', views.add_game, name='add_game'),
	path('games/', views.show_games, name='show_games'),
	path('games/<int:gid>/', views.show_game_info, name='show_game_info'),
	path('games/<int:gid>/edit/', views.edit_game, name='edit_game'),
	path('games/<int:gid>/add-comment/', views.add_comment, name='add_comment'),
	path('games/<int:gid>/<int:commid>/edit/', views.edit_comment, name='edit_comment'),
]