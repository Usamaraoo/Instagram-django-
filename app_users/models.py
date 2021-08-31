from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import date, datetime
from .manager import CustomUserManager
from datetime import datetime


class InstaUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    profile_pic = models.ImageField(null=True, blank=True)
    male = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=datetime.now)
    following = models.ManyToManyField('InstaUser', blank=True)
    followers = models.ManyToManyField(
        'InstaUser', related_name='InstaUser',  blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    # def save(self, *args, **kwargs):
    #     self.profile_pic.url = BASE_DIR+'/media/prof_pic'
    #     super().save(*args, **kwargs)


class Post(models.Model):
    post_img = models.ImageField(upload_to='posts/')
    description = models.CharField(max_length=300, null=True, blank=True)
    user = models.ForeignKey(
        InstaUser, related_name='user', null=True, on_delete=models.CASCADE)
    like = models.ManyToManyField(InstaUser, blank=True)

    def __str__(self):
        return self.description

    def get_comments(self):
        return Comment.objects.filter(post=self)


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    cmnt_user = models.ForeignKey(InstaUser, on_delete=models.CASCADE)
    gen_time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.comment


class Notification(models.Model):
    notify = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        InstaUser, related_name='notify', on_delete=models.CASCADE)
    from_user = models.ForeignKey(InstaUser, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    gen_time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.notify
