from django.contrib import admin
from .models import InstaUser, Post, Comment

admin.site.register(InstaUser)
admin.site.register(Post)
admin.site.register(Comment)
