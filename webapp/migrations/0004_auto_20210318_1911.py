# Generated by Django 3.0.7 on 2021-03-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20210318_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='photo',
            field=models.ImageField(upload_to='media/magazine/'),
        ),
    ]
