from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),
]
=======
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),

    # API real
    path("api/", include("core.urls")),

    # Redirección /api → /api/
    path("api", RedirectView.as_view(url="/api/", permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> a77a73ddba28b1b60b4ed6555f873c74ffe13654
