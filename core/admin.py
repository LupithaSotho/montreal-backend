from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Curso, Inscripcion, Certificacion

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "duracion_horas", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre",)


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "telefono", "curso", "nivel", "fecha_inicio", "nuevo_ingreso", "fecha_registro")
    list_filter = ("curso", "nivel", "nuevo_ingreso")
    search_fields = ("nombre", "correo", "telefono")


@admin.register(Certificacion)
class CertificacionAdmin(admin.ModelAdmin):
    list_display = ("folio", "alumno", "curso", "fecha_emision")
    search_fields = ("folio", "alumno")
>>>>>>> a77a73ddba28b1b60b4ed6555f873c74ffe13654
