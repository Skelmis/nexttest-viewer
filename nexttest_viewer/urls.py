from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "nexttest.koldfusion.xyz"
admin.site.site_title = "NextTest side administration"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
