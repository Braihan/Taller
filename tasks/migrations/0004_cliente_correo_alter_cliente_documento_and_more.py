# Generated by Django 4.2.6 on 2023-10-30 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_cliente_direccion_alter_cliente_documento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='documento',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.PositiveIntegerField(),
        ),
    ]
