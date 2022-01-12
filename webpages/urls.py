from django.urls import path

from . import views

urlpatterns = [
    path('', views.dash, name="dash"),
    path('users', views.users, name="users"),
    path('badges', views.badges, name="badges"),
    path('dashboard/<int:pk>/', views.dashboard, name="dashboard"),
    path('scratch/<int:pk>/', views.scratch, name="scratch"),
]