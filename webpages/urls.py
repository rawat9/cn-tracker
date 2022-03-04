from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users", views.users, name="users"),
    path("user/<int:pk>", views.user_profile, name="user"),
    path("add/", views.add_user, name="add"),
    path("edit/<int:pk>", views.edit_user, name="edit"),
    path("update/<int:pk>", views.update_user, name="update"),
    path("badges", views.badges, name="badges"),
    path("leaderboard", views.leaderboard, name="leaderboard"),
    
    # data-export
    path("export_excel", views.export_excel, name="export-excel"),
]
