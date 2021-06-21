from django.urls import path
from . import views

urlpatterns = [
    path('activityform', views.activity_form, name="activityform"), 
]   