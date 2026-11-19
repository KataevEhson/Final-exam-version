from django.urls import path, include
from .views import *


urlpatterns = [
    path('logout/', logout_user, name='logout'),
    path('leave/<int:pk>/', delete_game, name='leave'),
    path('search/', search, name='search'),
    path('games/', play_together, name='games'),
    path('join/<int:pk>/', join_game, name='join'),
    path('my/', my_stadium, name='my'),

    path('finish/<int:pk>/', finish_game, name='finish'),

    path('stadium_info/<int:pk>/', stadium_info, name='stadium_info'),
    path('book/<int:pk>/', book_stadium, name='book'),

    path('profile/', profile, name='profile'),
    path("", registration, name="register"),
    path("login/", login_user, name="login"),
    path('add', create_stadium, name='add'),
    path('show_stadiums', show_stadiums, name='show_stadiums'),
]



