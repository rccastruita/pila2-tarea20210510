from django.db import models
from django.conf import settings

# Create your models here.


def cv_image_path(instance, filename):
    return f"curriculum/foto_{instance.usuario.pk}_{filename}"


class Curriculum(models.Model):
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to=cv_image_path)
    educacion = models.CharField(max_length=60)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Experiencia(models.Model):
    nombre = models.CharField(max_length=50)
    tiempo_experiencia = models.CharField(max_length=20)
    descripcion = models.TextField()
    certificados = models.TextField(null=True, blank=True)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, related_name='experiencias')
