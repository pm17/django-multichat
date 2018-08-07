# Generated by Django 2.0.7 on 2018-08-06 05:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fil_auth', '0003_auto_20180806_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='idf',
            field=models.CharField(default=uuid.UUID('193d825c-3c6d-40b8-94dc-07c4f443dc1e'), max_length=64, verbose_name='Identification key'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_presenter',
            field=models.BooleanField(default=False),
        ),
    ]