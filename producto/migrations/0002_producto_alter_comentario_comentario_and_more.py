# Generated by Django 4.1.5 on 2023-01-22 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('producto', models.CharField(choices=[('celular', 'Celular'), ('notebook', 'Notebook'), ('televisor', 'Televisor'), ('heladera', 'Heladera'), ('lavarropa', 'Lavarropa'), ('otro', 'Otro')], default='Celular', max_length=15)),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fechaPublicacion', models.DateTimeField(auto_now_add=True)),
                ('telefonoContacto', models.IntegerField()),
                ('emailContacto', models.EmailField(max_length=254)),
                ('imagenProducto', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['usuario', '-fechaPublicacion'],
            },
        ),
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='producto.producto'),
        ),
        migrations.DeleteModel(
            name='Instrumento',
        ),
    ]