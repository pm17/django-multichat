# Generated by Django 2.0.7 on 2018-08-07 05:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20180806_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.CharField(default=uuid.UUID('8c9a4d8f-3fa8-4bbe-bba3-8bc7ad9a970b'), max_length=64, primary_key=True, serialize=False, verbose_name='Event Id'),
        ),
    ]
