from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    duracion_horas = models.PositiveIntegerField(default=20)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    nombre = models.CharField(max_length=140)
    correo = models.EmailField()
    telefono = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
<<<<<<< HEAD

    curso = models.CharField(max_length=120)      # Texto: “Inglés”
    nivel = models.CharField(max_length=120)      # Texto: “A2, B1...”

=======
    curso = models.CharField(max_length=120)          # Texto: "Inglés", "Computación", etc.
    nivel = models.CharField(max_length=120)          # Texto: "A2", "B1", etc.
>>>>>>> a77a73ddba28b1b60b4ed6555f873c74ffe13654
    fecha_inicio = models.DateField()
    nuevo_ingreso = models.BooleanField(default=True)
    comentarios = models.TextField(blank=True)

    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
<<<<<<< HEAD
        return f"{self.nombre} - {self.curso}"
=======
        return f"{self.nombre} - {self.curso} ({self.nivel})"
>>>>>>> a77a73ddba28b1b60b4ed6555f873c74ffe13654


class Certificacion(models.Model):
    alumno = models.CharField(max_length=140)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="certificaciones")
    folio = models.CharField(max_length=50, unique=True)
    fecha_emision = models.DateField()

    def __str__(self):
        return f"{self.alumno} - {self.folio}"
