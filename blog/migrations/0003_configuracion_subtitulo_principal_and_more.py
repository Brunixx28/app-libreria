# Generated by Django 4.1.2 on 2022-11-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_configuracion_construido_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='subtitulo_principal',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='titulo_principal',
            field=models.CharField(default='', max_length=30),
        ),
    ]
