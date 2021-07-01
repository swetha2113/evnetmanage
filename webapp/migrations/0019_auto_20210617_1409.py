# Generated by Django 3.0.7 on 2021-06-17 08:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0018_auto_20210617_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine',
            name='likes',
        ),
        migrations.AddField(
            model_name='magazine',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
