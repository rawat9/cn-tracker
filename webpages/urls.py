from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('users', views.users, name="users"),
    path('user/<int:pk>', views.user_profile, name="user"),
    path('badges', views.badges, name="badges"),
    path('leaderboard', views.leaderboard, name="leaderboard"),
]