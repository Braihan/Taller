from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models  import Tareas
# Register your models here.
class Tareasadmin(admin.ModelAdmin):
    readonly_fields = ("creado",)

admin.site.register(Tareas, Tareasadmin)
admin.site.register(Permission)
admin.site.register(ContentType)

