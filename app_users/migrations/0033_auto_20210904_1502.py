# Generated by Django 3.2.6 on 2021-09-04 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0032_auto_20210904_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gen_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 4, 15, 2, 48, 462066)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='gen_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 4, 15, 2, 48, 463275)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='gen_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 4, 15, 2, 48, 463852)),
        ),
    ]
