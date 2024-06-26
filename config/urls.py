from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.conf import settings

admin.site.site_header = "CODE NINJAS - North Finchley"
admin.site.index_title = "Admin Panel | Do Not Forget To Logout"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("webpages.urls")),
    path("auth/", include("authentication.urls")),
    path("activityform/", include("activityform.urls")),
    path("solutions/", include("solutions.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "webpages.views.error_404"
handler500 = "webpages.views.error_500"
