from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),

    # API
    path("api/", include("core.urls")),

    # Redirección opcional: /api → /api/
    path("api", RedirectView.as_view(url="/api/", permanent=True)),
]


# Archivos estáticos (solo en DEBUG)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
