# Generated by Django 3.2.6 on 2021-09-04 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0030_auto_20210904_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='gen_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 4, 14, 19, 22, 963054)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='gen_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 4, 14, 19, 22, 963543)),
        ),
    ]
