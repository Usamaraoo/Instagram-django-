from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.db.models.base import ModelState
from .manager import CustomUserManager
# fs = FileSystemStorage(location='/media/prof_pic')
from Instagram.settings import BASE_DIR


class InstaUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    profile_pic = models.ImageField(null=True, blank=True)
    male = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=datetime.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    # def save(self, *args, **kwargs):
    #     self.profile_pic.url = BASE_DIR+'/media/prof_pic'
    #     super().save(*args, **kwargs)
