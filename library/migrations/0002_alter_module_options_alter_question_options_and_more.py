# Generated by Django 5.0.2 on 2024-02-22 17:04

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'module', 'verbose_name_plural': 'modulos'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'pregunta', 'verbose_name_plural': 'preguntas'},
        ),
        migrations.AlterField(
            model_name='question',
            name='answer4',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='4'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Imagen de la pregunta'),
        ),
    ]