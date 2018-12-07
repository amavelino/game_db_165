from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('company/add/', views.add_company, name='add_company'),
	path('games/add-company-action/', views.add_company_action, name='add_company_action'),
	path('company/', views.show_company, name='show_company'),
	#path('company/<int:compid>', views.show_company_info, name='show_company_info'),
	path('company/<int:compid>/edit/', views.edit_company, name='edit_company'),
	path('company/<int:compid>/edit-action/', views.edit_company_action, name='edit_company_action'),

	path('games/', views.show_games, name='show_games'),
	path('games/add/', views.add_game, name='add_game'),
	path('games/add-game-action/', views.add_game_action, name='add_game_action'),
	path('games/<int:gid>/', views.show_game_info, name='show_game_info'),
	path('games/<int:gid>/edit/', views.edit_game, name='edit_game'),
	path('games/<int:gid>/edit-action/', views.edit_game_action, name='edit_game_action'),
	path('games/<int:gid>/delete/', views.delete_game, name='delete_game'),
	path('games/<int:gid>/add-comment/', views.add_comment, name='add_comment'),
	path('games/<int:gid>/<int:commid>/edit/', views.edit_comment, name='edit_comment'),
	path('games/<int:gid>/<int:commid>/delete/', views.delete_comment, name='delete_comment'),
]