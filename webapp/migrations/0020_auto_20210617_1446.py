# Generated by Django 3.0.7 on 2021-06-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_auto_20210617_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='createddate',
            field=models.DateField(auto_now_add=True),
        ),
    ]