# Generated by Django 4.2.6 on 2023-10-30 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_remove_tareas_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tareas',
            name='importante',
        ),
        migrations.RemoveField(
            model_name='tareas',
            name='user',
        ),
    ]
