# Generated by Django 4.1.5 on 2023-01-27 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='celular',
            old_name='emailContacto',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='celular',
            old_name='fechaPublicacion',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='celular',
            old_name='telefonoContacto',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='heladera',
            old_name='emailContacto',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='heladera',
            old_name='fechaPublicacion',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='heladera',
            old_name='telefonoContacto',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='lavarropa',
            old_name='emailContacto',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='lavarropa',
            old_name='fechaPublicacion',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='lavarropa',
            old_name='telefonoContacto',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='emailContacto',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='fechaPublicacion',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='telefonoContacto',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='televisor',
            old_name='emailContacto',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='televisor',
            old_name='fechaPublicacion',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='televisor',
            old_name='telefonoContacto',
            new_name='telefono',
        ),
    ]