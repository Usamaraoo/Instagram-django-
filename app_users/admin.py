from django.contrib import admin
from .models import InstaUser, Notification, Post, Comment

admin.site.register(InstaUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification)
