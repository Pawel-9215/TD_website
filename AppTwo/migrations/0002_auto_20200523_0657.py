# Generated by Django 3.0.3 on 2020-05-23 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='nick',
        ),
    ]