# Generated by Django 3.2 on 2023-04-02 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0003_auto_20230402_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='pilot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
