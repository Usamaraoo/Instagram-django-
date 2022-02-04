from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import date, datetime
from .manager import CustomUserManager
from datetime import datetime
from .validators import file_size
from mimetypes import guess_type


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

    # This method will return the profile image if exits otherwise set defaul
    def img_url(self):
        # Checking if the user is Facebook user or noraml user
        try:
            url = self.social_auth.get(
                provider='facebook').extra_data['picture']['data']['url']

            return url
        except:
            if self.profile_pic.name is '':
                return '/static/imgs/dp.png'
            else:
                return self.profile_pic.url


class Post(models.Model):
    post_img = models.FileField(upload_to='posts/', validators=[file_size])
    description = models.CharField(max_length=300, null=True, blank=True)
    gen_time = models.DateTimeField(default=datetime.now(), blank=True)
    user = models.ForeignKey(
        InstaUser, related_name='user', null=True, on_delete=models.CASCADE)
    like = models.ManyToManyField(InstaUser, blank=True)

    def __str__(self):
        return self.description

    def get_comments(self):
        return Comment.objects.filter(post=self)

    def media_type_html(self):
        """
        guess_type returns a tuple like (type, encoding) and we want to access
        the type of media file in first index of tuple
        """
        type_tuple = guess_type(self.post_img.url, strict=True)
        if (type_tuple[0]).__contains__("image"):
            return "image"
        elif (type_tuple[0]).__contains__("video"):
            return "video"


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


class Story(models.Model):
    story_img = models.FileField(upload_to='stories')
    story_user = models.ForeignKey(InstaUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.story_user.username
