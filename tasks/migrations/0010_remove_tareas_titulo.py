# Generated by Django 4.2.6 on 2023-10-30 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_rename_descripcion_tareas_observaciones_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tareas',
            name='titulo',
        ),
    ]
