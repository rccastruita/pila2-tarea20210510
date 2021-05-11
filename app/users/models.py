from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    buscando_empleo = models.BooleanField(default=True)
    ocupacion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
