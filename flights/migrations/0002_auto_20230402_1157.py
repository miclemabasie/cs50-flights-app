# Generated by Django 3.2 on 2023-04-02 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Flights',
            new_name='Flight',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='duratioin',
            new_name='duration',
        ),
    ]
