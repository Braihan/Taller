# Generated by Django 4.2.6 on 2023-11-08 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_alter_cliente_ruc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='direccion',
        ),
    ]
