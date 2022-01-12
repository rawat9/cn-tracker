from django.urls import path
from . import views

urlpatterns = [
    path('activityform/', views.activity_form, name="activityform"), 
    path('', views.act, name="activity"), 
    path('load_projects/', views.load_projects, name="ajax_load_projects"), 
]   