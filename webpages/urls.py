from django.urls import path

from . import views

urlpatterns = [
    path('', views.scorecard, name="scorecard"),
    path('dashboard/<str:pk>/', views.dashboard, name="dashboard"),
    path('scratch/<int:pk>/', views.scratch, name="scratch"),
    path('circuits/<int:pk>/', views.circuits, name="circuits"),
    path('artek/<int:pk>/', views.artek, name="artek"),
    path('lego/<int:pk>/', views.lego, name="lego"),
    path('typing/<int:pk>/', views.typing, name="typing"),
]