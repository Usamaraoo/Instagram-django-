# Generated by Django 3.2.6 on 2022-01-29 15:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0033_auto_20210904_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='gen_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 29, 20, 11, 29, 248642)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='gen_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 29, 20, 11, 29, 249130)),
        ),
        migrations.AlterField(
            model_name='post',
            name='gen_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 29, 20, 11, 29, 247551)),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_img', models.FileField(upload_to='stories')),
                ('story_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]