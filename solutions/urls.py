from django.urls import path

from . import views

urlpatterns = [
    path("cc-python", views.cc_python, name="cc-python"),
]
