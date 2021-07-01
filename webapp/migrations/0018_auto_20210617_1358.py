# Generated by Django 3.0.7 on 2021-06-17 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_magazine_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine',
            name='likes',
        ),
        migrations.AddField(
            model_name='magazine',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
