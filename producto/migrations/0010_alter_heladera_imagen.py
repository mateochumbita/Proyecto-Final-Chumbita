# Generated by Django 4.1.5 on 2023-01-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0009_alter_celular_imagen_alter_heladera_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heladera',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]