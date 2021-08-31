"""cntracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# 2FA
# from django_otp.admin import OTPAdminSite
# admin.site.__class__ = OTPAdminSite

admin.site.site_header = "CODE NINJAS - North Finchley"
admin.site.index_title = "Admin Panel | Do Not Forget To Logout"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webpages.urls')),
    path('authentication/', include('authentication.urls')),
    path('activityform/', include('activityform.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

