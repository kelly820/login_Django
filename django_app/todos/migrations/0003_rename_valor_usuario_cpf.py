# Generated by Django 5.1 on 2024-08-27 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='valor',
            new_name='cpf',
        ),
    ]
