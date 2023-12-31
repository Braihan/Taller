# Generated by Django 4.2.6 on 2023-10-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_rename_cliente_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('documento', models.PositiveIntegerField()),
                ('telefono', models.PositiveIntegerField()),
                ('direccion', models.TextField()),
                ('correo', models.EmailField(default='example@example.com', max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
    ]
