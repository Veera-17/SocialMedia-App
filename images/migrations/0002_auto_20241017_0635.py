# Generated by Django 3.0 on 2024-10-17 06:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Images',
        ),
    ]
