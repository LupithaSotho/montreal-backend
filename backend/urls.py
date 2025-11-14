from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import CursoViewSet, InscripcionViewSet, CertificacionViewSet
<<<<<<< HEAD
# ajusta "core" al nombre real de tu app
=======
from django.conf import settings
from django.conf.urls.static import static  # 👈 Import necesario
>>>>>>> e546fd0acd8c7666647ddba48bafcc734faa4b29

router = DefaultRouter()
router.register(r"cursos", CursoViewSet, basename="curso")
router.register(r"inscripciones", InscripcionViewSet, basename="inscripcion")
router.register(r"certificaciones", CertificacionViewSet, basename="certificacion")

urlpatterns = [
<<<<<<< HEAD
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
=======
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
>>>>>>> e546fd0acd8c7666647ddba48bafcc734faa4b29
