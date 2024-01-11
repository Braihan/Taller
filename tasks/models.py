from django.db import models
from django.core.validators import RegexValidator
# Create your models here. para la base de datos
class Tareas(models.Model):
    trabajosolicitado = models.TextField(blank=True)
    trabajoarealizar = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    completado = models.DateTimeField(null=True, blank=True)
    nombre = models.CharField(max_length=255)
    telefono =  models.PositiveIntegerField(default=0)
    
class Cliente(models.Model):
    nombre = models.TextField(blank=False)
    documento = models.PositiveIntegerField(blank=False, validators=[RegexValidator(r'^[0-9]+$')])
    telefono =  models.PositiveIntegerField(blank=False, validators=[RegexValidator(r'^[0-9]{9,12}$')])
    correo = models.EmailField(blank=False)
    ruc = models.CharField(max_length=25, null=True, validators=[RegexValidator(regex=r'^[0-9-]+$')])
    
    
    def __str__(self):
        return self.titulo + ' - ' + self.user.username