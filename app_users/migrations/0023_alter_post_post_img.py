# Generated by Django 3.2.6 on 2021-08-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0022_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
